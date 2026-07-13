import tomllib
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def test_poetry_metadata_uses_only_public_pypi():
    pyproject = tomllib.loads((ROOT / "pyproject.toml").read_text(encoding="utf-8"))

    assert "source" not in pyproject["tool"]["poetry"]


def test_lockfile_resolves_sdk_from_public_pypi():
    lock = tomllib.loads((ROOT / "poetry.lock").read_text(encoding="utf-8"))
    sdk = next(package for package in lock["package"] if package["name"] == "maltego-transforms")

    assert sdk["version"] == "1.0.0"
    assert all("source" not in package for package in lock["package"])
