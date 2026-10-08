#!/usr/bin/env python3
"""Query the deterministic lexical retrieval index."""

from __future__ import annotations

import argparse
import json
from collections import defaultdict
from pathlib import Path

from build_lexical_retrieval import normalize, tokens


def load_jsonl(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line]


def search(index: dict, units: list[dict], query: str, limit: int = 10) -> list[dict]:
    unit_by_ordinal = {row["index_ordinal"]: row for row in units}
    unit_scores: dict[int, float] = defaultdict(float)
    k1 = index["algorithm"]["k1"]
    b = index["algorithm"]["b"]
    avgdl = index["corpus"]["average_unit_length"]
    normalized = normalize(query)
    qterms = sorted(set(tokens(query)))

    exact_doc_ids: list[str] = []
    for bucket in ("exact_title", "exact_path"):
        exact_doc_ids.extend(index[bucket].get(normalized, []))
    exact_doc_ids = list(dict.fromkeys(exact_doc_ids))

    for term in qterms:
        entry = index["terms"].get(term)
        if not entry:
            continue
        idf = entry["idf"]
        for unit_ordinal, tf in entry["postings"]:
            unit = unit_by_ordinal[unit_ordinal]
            dl = unit["token_count"]
            denominator = tf + k1 * (1 - b + b * dl / avgdl)
            unit_scores[unit_ordinal] += idf * (tf * (k1 + 1)) / denominator

    ranked: list[dict] = []
    seen_units: set[int] = set()
    for doc_id in exact_doc_ids:
        unit_ordinal = index["doc_first_unit"][doc_id]
        unit = unit_by_ordinal[unit_ordinal]
        document = index["documents"][doc_id]
        ranked.append(
            {
                "rank_reason": "EXACT_FIRST",
                "score": None,
                "unit_id": unit["unit_id"],
                "doc_id": doc_id,
                "source_path": document["source_path"],
                "title": document["title"],
                "heading_path": unit["heading_path"],
                "text": unit["text"],
            }
        )
        seen_units.add(unit_ordinal)

    for unit_ordinal, score in sorted(
        unit_scores.items(),
        key=lambda item: (
            -item[1],
            index["documents"][unit_by_ordinal[item[0]]["doc_id"]]["source_path"],
            unit_by_ordinal[item[0]]["sequence"],
        ),
    ):
        if unit_ordinal in seen_units:
            continue
        unit = unit_by_ordinal[unit_ordinal]
        document = index["documents"][unit["doc_id"]]
        ranked.append(
            {
                "rank_reason": "BM25",
                "score": round(score, 12),
                "unit_id": unit["unit_id"],
                "doc_id": unit["doc_id"],
                "source_path": document["source_path"],
                "title": document["title"],
                "heading_path": unit["heading_path"],
                "text": unit["text"],
            }
        )
        if len(ranked) >= limit:
            break
    return ranked[:limit]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("query")
    parser.add_argument("--index", type=Path, default=Path("governanca/retrieval/LEXICAL_INDEX.json"))
    parser.add_argument("--units", type=Path, default=Path("governanca/retrieval/RETRIEVAL_UNITS.jsonl"))
    parser.add_argument("--limit", type=int, default=10)
    args = parser.parse_args()
    index = json.loads(args.index.read_text(encoding="utf-8"))
    units = load_jsonl(args.units)
    for row in search(index, units, args.query, args.limit):
        print(json.dumps(row, ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    main()

