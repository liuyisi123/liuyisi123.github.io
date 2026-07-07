#!/usr/bin/env python3
"""Refresh Google Scholar metrics used by the homepage badges."""

from __future__ import annotations

import json
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path


SCHOLAR_URL = "https://scholar.google.com/citations?user=IU9omVgAAAAJ&hl=en"
OUTPUT = Path("assets/data/scholar-metrics.json")
FALLBACK = {"citations": "400+", "hIndex": "10"}


def fetch_profile() -> str:
    request = urllib.request.Request(
        SCHOLAR_URL,
        headers={
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120 Safari/537.36"
            )
        },
    )
    with urllib.request.urlopen(request, timeout=20) as response:
        return response.read().decode("utf-8", errors="replace")


def parse_metrics(html: str) -> dict[str, str]:
    rows = re.findall(
        r"<td class=\"gsc_rsb_sc1\">(Citations|h-index)</td>\s*"
        r"<td class=\"gsc_rsb_std\">([^<]+)</td>",
        html,
        flags=re.IGNORECASE,
    )
    metrics: dict[str, str] = {}
    for label, value in rows:
        value = value.strip().replace(",", "")
        if not value:
            continue
        if label.lower() == "citations":
            metrics["citations"] = value
        elif label.lower() == "h-index":
            metrics["hIndex"] = value
    return metrics


def read_existing() -> dict[str, str]:
    if not OUTPUT.exists():
        return FALLBACK.copy()
    try:
        with OUTPUT.open("r", encoding="utf-8") as handle:
            data = json.load(handle)
        return {
            "citations": str(data.get("citations") or FALLBACK["citations"]),
            "hIndex": str(data.get("hIndex") or FALLBACK["hIndex"]),
        }
    except (OSError, json.JSONDecodeError):
        return FALLBACK.copy()


def main() -> int:
    existing = read_existing()
    try:
        metrics = parse_metrics(fetch_profile())
    except (urllib.error.URLError, TimeoutError, ValueError) as exc:
        print(f"Could not refresh Google Scholar metrics: {exc}", file=sys.stderr)
        metrics = {}

    output = {
        "citations": metrics.get("citations") or existing["citations"],
        "hIndex": metrics.get("hIndex") or existing["hIndex"],
    }

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(output, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(output, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
