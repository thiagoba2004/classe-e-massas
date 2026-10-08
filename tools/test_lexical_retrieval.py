#!/usr/bin/env python3
"""Validate integrity, determinism, and retrieval quality for EA-000001-000036."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import tempfile
from pathlib import Path

from build_lexical_retrieval import build
from query_lexical_retrieval import load_jsonl, search


ARTIFACTS = (
    "RETRIEVAL_DOCUMENTS.jsonl",
    "RETRIEVAL_UNITS.jsonl",
    "LEXICAL_INDEX.json",
)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def validate_integrity(root: Path, documents: list[dict], units: list[dict], index: dict) -> list[str]:
    errors: list[str] = []
    doc_ids = [d["doc_id"] for d in documents]
    unit_ids = [u["unit_id"] for u in units]
    if len(doc_ids) != len(set(doc_ids)):
        errors.append("duplicate document IDs")
    if len(unit_ids) != len(set(unit_ids)):
        errors.append("duplicate unit IDs")
    if index["corpus"]["documents"] != len(documents):
        errors.append("document count mismatch")
    if index["corpus"]["units"] != len(units):
        errors.append("unit count mismatch")
    known_docs = set(doc_ids)
    for doc in documents:
        raw = (root / doc["source_path"]).read_text(encoding="utf-8")
        if hashlib.sha256(raw.encode("utf-8")).hexdigest() != doc["source_sha256"]:
            errors.append(f'source hash mismatch: {doc["source_path"]}')
    for unit in units:
        if unit["doc_id"] not in known_docs:
            errors.append(f'orphan unit: {unit["unit_id"]}')
        if hashlib.sha256(unit["text"].encode("utf-8")).hexdigest() != unit["text_sha256"]:
            errors.append(f'text hash mismatch: {unit["unit_id"]}')
    return errors


def determinism_check(root: Path, baseline: Path) -> dict:
    with tempfile.TemporaryDirectory() as temp:
        base = Path(temp)
        first = base / "first"
        second = base / "second"
        build(root, baseline, first, "2026-10-08T00:00:00Z")
        build(root, baseline, second, "2026-10-08T00:00:00Z")
        comparisons = {
            name: {
                "first_sha256": sha256(first / name),
                "second_sha256": sha256(second / name),
                "identical": (first / name).read_bytes() == (second / name).read_bytes(),
            }
            for name in ARTIFACTS
        }
    return {
        "passed": all(row["identical"] for row in comparisons.values()),
        "artifacts": comparisons,
    }


def evaluate(cases: list[dict], index: dict, units: list[dict]) -> dict:
    per_case: list[dict] = []
    reciprocal_ranks: list[float] = []
    recalls: list[float] = []
    ndcgs: list[float] = []
    positive_hits = 0
    negatives_passed = 0
    negative_count = 0
    exact_passed = 0
    exact_count = 0

    for case in cases:
        results = search(index, units, case["query"], case["k"])
        paths = [row["source_path"] for row in results]
        expected = case["expected_paths"]
        if not expected:
            negative_count += 1
            passed = len(results) == 0
            negatives_passed += int(passed)
            per_case.append(
                {
                    "id": case["id"],
                    "dimension": case["dimension"],
                    "query": case["query"],
                    "expected_paths": expected,
                    "returned_paths": paths,
                    "passed": passed,
                }
            )
            continue

        first_rank = next(
            (rank for rank, path in enumerate(paths, start=1) if path in expected),
            None,
        )
        retrieved_expected = len(set(paths) & set(expected))
        recall = retrieved_expected / len(expected)
        rr = 0.0 if first_rank is None else 1.0 / first_rank
        ndcg = 0.0 if first_rank is None else 1.0 / math.log2(first_rank + 1)
        exact_ok = None
        if case.get("exact_first_required"):
            exact_count += 1
            exact_ok = bool(results and results[0]["rank_reason"] == "EXACT_FIRST" and paths[0] in expected)
            exact_passed += int(exact_ok)
        reciprocal_ranks.append(rr)
        recalls.append(recall)
        ndcgs.append(ndcg)
        positive_hits += int(first_rank is not None)
        per_case.append(
            {
                "id": case["id"],
                "dimension": case["dimension"],
                "query": case["query"],
                "expected_paths": expected,
                "returned_paths": paths,
                "first_relevant_rank": first_rank,
                "recall_at_k": recall,
                "reciprocal_rank": rr,
                "ndcg_at_k": ndcg,
                "exact_first_passed": exact_ok,
                "passed": first_rank is not None and (exact_ok is not False),
            }
        )

    positive_count = len(reciprocal_ranks)
    return {
        "cases": len(cases),
        "positive_cases": positive_count,
        "negative_cases": negative_count,
        "metrics": {
            "recall_at_5": sum(recalls) / positive_count,
            "mrr": sum(reciprocal_ranks) / positive_count,
            "ndcg_at_5": sum(ndcgs) / positive_count,
            "evidence_hit_rate": positive_hits / positive_count,
            "negative_pass_rate": negatives_passed / negative_count if negative_count else 1.0,
            "exact_first_rate": exact_passed / exact_count if exact_count else 1.0,
        },
        "per_case": per_case,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path("."))
    parser.add_argument("--baseline", type=Path, default=Path("governanca/retrieval/F1_BASELINE.json"))
    parser.add_argument("--retrieval-dir", type=Path, default=Path("governanca/retrieval"))
    parser.add_argument("--cases", type=Path, default=Path("governanca/retrieval/LEXICAL_TEST_CASES.jsonl"))
    parser.add_argument("--output", type=Path, default=Path("governanca/retrieval/LEXICAL_BENCHMARK_RESULT.json"))
    args = parser.parse_args()

    documents = load_jsonl(args.retrieval_dir / "RETRIEVAL_DOCUMENTS.jsonl")
    units = load_jsonl(args.retrieval_dir / "RETRIEVAL_UNITS.jsonl")
    cases = load_jsonl(args.cases)
    index = json.loads((args.retrieval_dir / "LEXICAL_INDEX.json").read_text(encoding="utf-8"))

    integrity_errors = validate_integrity(args.root, documents, units, index)
    determinism = determinism_check(args.root, args.baseline)
    evaluation = evaluate(cases, index, units)
    thresholds = {
        "recall_at_5_min": 1.0,
        "mrr_min": 0.95,
        "ndcg_at_5_min": 0.95,
        "evidence_hit_rate_min": 1.0,
        "negative_pass_rate_min": 1.0,
        "exact_first_rate_min": 1.0,
        "integrity_errors_max": 0,
        "deterministic_rebuild_required": True,
    }
    metrics = evaluation["metrics"]
    gate_checks = {
        "recall_at_5": metrics["recall_at_5"] >= thresholds["recall_at_5_min"],
        "mrr": metrics["mrr"] >= thresholds["mrr_min"],
        "ndcg_at_5": metrics["ndcg_at_5"] >= thresholds["ndcg_at_5_min"],
        "evidence_hit_rate": metrics["evidence_hit_rate"] >= thresholds["evidence_hit_rate_min"],
        "negative_pass_rate": metrics["negative_pass_rate"] >= thresholds["negative_pass_rate_min"],
        "exact_first_rate": metrics["exact_first_rate"] >= thresholds["exact_first_rate_min"],
        "integrity": not integrity_errors,
        "deterministic_rebuild": determinism["passed"],
    }
    report = {
        "schema_version": "1.0",
        "strategy_code": "EA-000001-000036",
        "generated_at": "2026-10-08T00:00:00Z",
        "corpus": index["corpus"],
        "thresholds": thresholds,
        "evaluation": evaluation,
        "integrity": {"passed": not integrity_errors, "errors": integrity_errors},
        "determinism": determinism,
        "gate_checks": gate_checks,
        "gate_status": "PASSED" if all(gate_checks.values()) else "FAILED",
    }
    args.output.write_text(
        json.dumps(report, ensure_ascii=False, sort_keys=True, indent=2) + "\n",
        encoding="utf-8",
    )
    print(json.dumps({"gate_status": report["gate_status"], **metrics}, sort_keys=True))
    if report["gate_status"] != "PASSED":
        raise SystemExit(1)


if __name__ == "__main__":
    main()

