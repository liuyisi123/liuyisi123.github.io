#!/usr/bin/env python3
"""Refresh Google Scholar metrics used by the homepage badges."""

from __future__ import annotations

import json
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

try:
    import requests
    from bs4 import BeautifulSoup
except ImportError:  # Local fallback; GitHub Actions installs these packages.
    requests = None
    BeautifulSoup = None
    import urllib.error
    import urllib.request

REQUEST_ERRORS = (OSError,) if requests is None else (OSError, requests.RequestException)
REFRESH_ERRORS = (RuntimeError, TimeoutError, ValueError) + REQUEST_ERRORS


SCHOLAR_ID = os.environ.get("GOOGLE_SCHOLAR_ID", "IU9omVgAAAAJ")
SCHOLAR_URL = f"https://scholar.google.com/citations?user={SCHOLAR_ID}&hl=en"
PRIMARY_OUTPUT = Path("google-scholar-stats/gs_data.json")
LEGACY_OUTPUT = Path("assets/data/scholar-metrics.json")
FALLBACK = {
    "name": "Jian Liu",
    "scholar_id": SCHOLAR_ID,
    "updated": "",
    "citedby": "400+",
    "hindex": 10,
    "i10index": "",
}


def fetch_profile() -> str:
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120 Safari/537.36"
        )
    }
    if requests is None:
        request = urllib.request.Request(SCHOLAR_URL, headers=headers)
        with urllib.request.urlopen(request, timeout=25) as response:
            return response.read().decode("utf-8", errors="replace")

    response = requests.get(
        SCHOLAR_URL,
        headers=headers,
        timeout=30,
    )
    response.raise_for_status()
    return response.text


def parse_metrics(html: str) -> dict[str, int | str]:
    if "recaptcha" in html.lower() or "unusual traffic" in html.lower():
        raise RuntimeError("Google Scholar returned captcha / unusual traffic page.")

    metrics: dict[str, int | str] = {}
    if BeautifulSoup is not None:
        soup = BeautifulSoup(html, "html.parser")
        name_tag = soup.select_one("#gsc_prf_in")
        rows = soup.select("table#gsc_rsb_st tbody tr")
        for row in rows:
            cells = row.select("td")
            if len(cells) < 2:
                continue
            label = cells[0].get_text(strip=True).lower()
            value = cells[1].get_text(strip=True)
            digits = re.sub(r"[^\d]", "", value)
            parsed = int(digits) if digits else 0
            if "citation" in label:
                metrics["citedby"] = parsed
            elif "h-index" in label:
                metrics["hindex"] = parsed
            elif "i10-index" in label:
                metrics["i10index"] = parsed
        name = name_tag.get_text(strip=True) if name_tag else FALLBACK["name"]
    else:
        name_match = re.search(r'<div id="gsc_prf_in">([^<]+)</div>', html)
        rows = re.findall(
            r"<td class=\"gsc_rsb_sc1\">(Citations|h-index|i10-index)</td>\s*"
            r"<td class=\"gsc_rsb_std\">([^<]+)</td>",
            html,
            flags=re.IGNORECASE,
        )
        for label, value in rows:
            digits = re.sub(r"[^\d]", "", value)
            parsed = int(digits) if digits else 0
            key = label.lower()
            if key == "citations":
                metrics["citedby"] = parsed
            elif key == "h-index":
                metrics["hindex"] = parsed
            elif key == "i10-index":
                metrics["i10index"] = parsed
        name = name_match.group(1).strip() if name_match else FALLBACK["name"]

    if not metrics:
        raise RuntimeError("Failed to parse Google Scholar statistics table.")

    metrics["name"] = name
    return metrics


def read_existing() -> dict[str, int | str]:
    for path in (PRIMARY_OUTPUT, LEGACY_OUTPUT):
        if not path.exists():
            continue
        try:
            with path.open("r", encoding="utf-8") as handle:
                data = json.load(handle)
            return {
                "name": str(data.get("name") or FALLBACK["name"]),
                "scholar_id": str(data.get("scholar_id") or SCHOLAR_ID),
                "updated": str(data.get("updated") or ""),
                "citedby": data.get("citedby") or data.get("citations") or FALLBACK["citedby"],
                "hindex": data.get("hindex") or data.get("hIndex") or FALLBACK["hindex"],
                "i10index": data.get("i10index") or data.get("i10Index") or FALLBACK["i10index"],
            }
        except (OSError, json.JSONDecodeError):
            continue
    return FALLBACK.copy()


def write_json(path: Path, data: dict[str, int | str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main() -> int:
    existing = read_existing()
    try:
        scraped = parse_metrics(fetch_profile())
        updated = datetime.now(timezone.utc).date().isoformat()
    except REFRESH_ERRORS as exc:
        print(f"Could not refresh Google Scholar metrics: {exc}", file=sys.stderr)
        scraped = {}
        updated = str(existing.get("updated") or "")

    primary = {
        "name": scraped.get("name") or existing["name"],
        "scholar_id": SCHOLAR_ID,
        "updated": updated,
        "citedby": scraped.get("citedby") or existing["citedby"],
        "hindex": scraped.get("hindex") or existing["hindex"],
        "i10index": scraped.get("i10index") or existing["i10index"],
    }
    legacy = {
        "citations": primary["citedby"],
        "hIndex": primary["hindex"],
        "i10Index": primary["i10index"],
    }

    write_json(PRIMARY_OUTPUT, primary)
    write_json(LEGACY_OUTPUT, legacy)
    print(json.dumps(primary, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
