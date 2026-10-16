import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
README_PATH = REPO_ROOT / "README.md"

FLAGSHIP_REPOS = [
    "annotatoriq-data-quality-ops",
    "rag-reliability-observatory",
    "preferenceforge-alignment-study",
    "documentvision-multimodal-benchmark",
    "agentbench-works",
    "trustboundary-ai-security-lab",
    "temporal-grounding-lab",
]


def test_readme_exists():
    assert README_PATH.is_file(), "README.md must exist in the portfolio root"
    content = README_PATH.read_text(encoding="utf-8")
    assert len(content) > 1000, "README.md should have substantial content"


def test_all_flagship_repos_referenced():
    content = README_PATH.read_text(encoding="utf-8")
    for repo_name in FLAGSHIP_REPOS:
        expected_link = f"https://github.com/master72o/{repo_name}"
        assert expected_link in content, f"README must link to flagship {repo_name}"


def test_markdown_links_well_formed():
    content = README_PATH.read_text(encoding="utf-8")
    links = re.findall(r"\[([^\]]+)\]\((https?://[^\)]+)\)", content)
    assert len(links) >= 15, "Expected at least 15 outbound links in the catalog"
    for text, url in links:
        assert url.startswith("http://") or url.startswith("https://"), f"Invalid url {url}"


def test_mermaid_diagram_present_and_valid():
    content = README_PATH.read_text(encoding="utf-8")
    assert "```mermaid" in content, "README must contain the architecture Mermaid diagram"
    assert "graph TD" in content or "graph LR" in content, "Mermaid diagram must specify directional graph"


def test_license_and_python_badges():
    content = README_PATH.read_text(encoding="utf-8")
    assert "Python-3.10" in content, "Python 3.10+ badge must be present"
    assert "License-MIT" in content, "MIT License badge must be present"
