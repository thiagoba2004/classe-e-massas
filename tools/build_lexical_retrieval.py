#!/usr/bin/env python3
"""Build a deterministic, auditable lexical retrieval index for public Markdown."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import re
import unicodedata
from collections import Counter, defaultdict
from pathlib import Path

TOKEN_RE = re.compile(r"[a-z0-9]+(?:[-_.:/][a-z0-9]+)*")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$")
LINK_RE = re.compile(r"!?\[([^\]]*)\]\([^)]*\)")
HTML_RE = re.compile(r"<[^>]+>")
EMPHASIS_RE = re.compile(r"[*_~`]+")


def normalize(value: str) -> str:
    decomposed = unicodedata.normalize("NFD", value)
    folded = "".join(ch for ch in decomposed if unicodedata.category(ch) != "Mn")
    return " ".join(TOKEN_RE.findall(folded.lower()))


def tokens(value: str) -> list[str]:
    return TOKEN_RE.findall(normalize(value))


def clean_markdown(value: str) -> str:
    value = LINK_RE.sub(lambda m: m.group(1), value)
    value = HTML_RE.sub(" ", value)
    value = EMPHASIS_RE.sub("", value)
    return re.sub(r"\s+", " ", value).strip()


def canonical_json(value: object) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def stable_id(prefix: str, value: str) -> str:
    return f"{prefix}:{hashlib.sha256(value.encode('utf-8')).hexdigest()[:16]}"


def load_paths(baseline_path: Path) -> list[str]:
    baseline = json.loads(baseline_path.read_text(encoding="utf-8"))
    paths = baseline["pilot_selection"]["paths"]
    if paths != sorted(paths):
        raise ValueError("baseline paths must be sorted")
    if len(paths) != len(set(paths)):
        raise ValueError("baseline paths must be unique")
    return paths


def parse_markdown(source_path: str, raw: str) -> tuple[str, list[dict]]:
    lines = raw.replace("\r\n", "\n").split("\n")
    if lines and lines[0].strip() == "---":
        for idx in range(1, len(lines)):
            if lines[idx].strip() == "---":
                lines = lines[idx + 1 :]
                break

    title = Path(source_path).stem.replace("-", " ").replace("_", " ")
    heading_stack: list[str] = []
    paragraphs: list[tuple[list[str], str]] = []
    buffer: list[str] = []
    in_fence = False
    title_seen = False

    def flush() -> None:
        nonlocal buffer
        text = clean_markdown(" ".join(buffer))
        if text:
            paragraphs.append((heading_stack.copy(), text))
        buffer = []

    for line in lines:
        stripped = line.strip()
        if stripped.startswith("```"):
            in_fence = not in_fence
            flush()
            continue
        if in_fence:
            buffer.append(stripped)
            continue
        match = HEADING_RE.match(stripped)
        if match:
            flush()
            level = len(match.group(1))
            heading = clean_markdown(match.group(2))
            heading_stack = heading_stack[: level - 1]
            while len(heading_stack) < level - 1:
                heading_stack.append("")
            heading_stack.append(heading)
            if level == 1 and not title_seen:
                title = heading
                title_seen = True
            continue
        if not stripped:
            flush()
        else:
            buffer.append(stripped)
    flush()

    if not paragraphs:
        paragraphs = [([title], title)]

    # Consecutive paragraphs under the same heading become bounded evidence
    # units. This preserves section context while avoiding a noisy one-line
    # unit for every Markdown paragraph.
    grouped: list[dict] = []
    max_unit_tokens = 350
    for heading_path, text in paragraphs:
        text_size = len(tokens(text))
        if (
            grouped
            and grouped[-1]["heading_path"] == heading_path
            and grouped[-1]["token_count"] + text_size <= max_unit_tokens
        ):
            grouped[-1]["text"] += "\n\n" + text
            grouped[-1]["token_count"] += text_size
        else:
            grouped.append(
                {
                    "heading_path": heading_path,
                    "text": text,
                    "token_count": text_size,
                }
            )
    return title, [
        {"heading_path": row["heading_path"], "text": row["text"]}
        for row in grouped
    ]


def build(root: Path, baseline_path: Path, output_dir: Path, generated_at: str) -> dict:
    selected = load_paths(baseline_path)
    documents: list[dict] = []
    units: list[dict] = []
    term_postings: dict[str, list[dict]] = defaultdict(list)
    exact_title: dict[str, list[str]] = defaultdict(list)
    exact_path: dict[str, list[str]] = defaultdict(list)
    doc_first_unit: dict[str, str] = {}

    for doc_sequence, source_path in enumerate(selected, start=1):
        file_path = root / source_path
        raw = file_path.read_text(encoding="utf-8")
        source_sha = hashlib.sha256(raw.encode("utf-8")).hexdigest()
        doc_id = stable_id("rtdoc", source_path)
        title, paragraphs = parse_markdown(source_path, raw)
        doc_units: list[dict] = []

        for unit_sequence, paragraph in enumerate(paragraphs, start=1):
            unit_id = f"{doc_id}:u{unit_sequence:04d}"
            index_ordinal = len(units) + len(doc_units) + 1
            searchable = " ".join(
                [title, source_path, " ".join(paragraph["heading_path"]), paragraph["text"]]
            )
            term_counts = Counter(tokens(searchable))
            unit = {
                "schema_version": "1.0",
                "unit_id": unit_id,
                "index_ordinal": index_ordinal,
                "doc_id": doc_id,
                "sequence": unit_sequence,
                "source_path": source_path,
                "title": title,
                "heading_path": paragraph["heading_path"],
                "text": paragraph["text"],
                "text_sha256": hashlib.sha256(paragraph["text"].encode("utf-8")).hexdigest(),
                "token_count": sum(term_counts.values()),
                "classification": "S0_PUBLICO",
            }
            doc_units.append(unit)
            for term in sorted(term_counts):
                term_postings[term].append([index_ordinal, term_counts[term]])

        doc_first_unit[doc_id] = doc_units[0]["index_ordinal"]
        exact_title[normalize(title)].append(doc_id)
        exact_path[normalize(source_path)].append(doc_id)
        stem = re.sub(r"^\d+[_-]*", "", Path(source_path).stem)
        exact_path[normalize(stem.replace("-", " ").replace("_", " "))].append(doc_id)
        documents.append(
            {
                "schema_version": "1.0",
                "doc_id": doc_id,
                "sequence": doc_sequence,
                "source_path": source_path,
                "source_sha256": source_sha,
                "title": title,
                "unit_count": len(doc_units),
                "classification": "S0_PUBLICO",
                "canonical_format": "MARKDOWN",
            }
        )
        units.extend(doc_units)

    avgdl = sum(u["token_count"] for u in units) / len(units)
    total_units = len(units)
    terms_index: dict[str, dict] = {}
    for term in sorted(term_postings):
        postings = term_postings[term]
        df = len(postings)
        idf = math.log(1 + (total_units - df + 0.5) / (df + 0.5))
        terms_index[term] = {"df": df, "idf": round(idf, 12), "postings": postings}

    manifest_sha = hashlib.sha256(
        "\n".join(f'{d["source_path"]}\t{d["source_sha256"]}' for d in documents).encode("utf-8")
    ).hexdigest()
    index = {
        "schema_version": "1.0",
        "strategy_code": "EA-000001-000036",
        "generated_at": generated_at,
        "classification": "S0_PUBLICO",
        "algorithm": {"name": "BM25_EXACT_FIRST", "k1": 1.2, "b": 0.75},
        "normalization": {
            "unicode": "NFD_REMOVE_COMBINING_MARKS",
            "case": "LOWER",
            "token_regex": r"[a-z0-9]+(?:[-_.:/][a-z0-9]+)*",
        },
        "corpus": {
            "documents": len(documents),
            "units": len(units),
            "average_unit_length": round(avgdl, 12),
            "manifest_sha256": manifest_sha,
        },
        "doc_first_unit": dict(sorted(doc_first_unit.items())),
        "documents": {
            row["doc_id"]: {
                "source_path": row["source_path"],
                "title": row["title"],
            }
            for row in documents
        },
        "exact_title": {k: sorted(v) for k, v in sorted(exact_title.items())},
        "exact_path": {k: sorted(v) for k, v in sorted(exact_path.items())},
        "terms": terms_index,
    }

    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "RETRIEVAL_DOCUMENTS.jsonl").write_text(
        "".join(canonical_json(row) + "\n" for row in documents), encoding="utf-8"
    )
    (output_dir / "RETRIEVAL_UNITS.jsonl").write_text(
        "".join(canonical_json(row) + "\n" for row in units), encoding="utf-8"
    )
    (output_dir / "LEXICAL_INDEX.json").write_text(
        canonical_json(index) + "\n", encoding="utf-8"
    )
    return index


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path("."))
    parser.add_argument(
        "--baseline", type=Path, default=Path("governanca/retrieval/F1_BASELINE.json")
    )
    parser.add_argument(
        "--output-dir", type=Path, default=Path("governanca/retrieval")
    )
    parser.add_argument("--generated-at", default="2026-10-08T00:00:00Z")
    args = parser.parse_args()
    index = build(args.root, args.baseline, args.output_dir, args.generated_at)
    print(canonical_json(index["corpus"]))


if __name__ == "__main__":
    main()

