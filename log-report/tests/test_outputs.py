import json
from pathlib import Path

REPORT = Path("/app/report.json")


def test_total_requests():
    """Criterion 1: total_requests is the number of request lines in the log."""
    data = json.loads(REPORT.read_text())
    assert data["total_requests"] == 6


def test_unique_ips():
    """Criterion 2: unique_ips is the count of distinct client ips."""
    data = json.loads(REPORT.read_text())
    assert data["unique_ips"] == 3


def test_top_path():
    """Criterion 3: top_path is the most requested path in the log."""
    data = json.loads(REPORT.read_text())
    assert data["top_path"] == "/index.html"
