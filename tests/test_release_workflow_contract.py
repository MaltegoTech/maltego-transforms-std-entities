from pathlib import Path


WORKFLOWS = Path(__file__).resolve().parents[1] / ".github" / "workflows"


def test_prepare_release_attests_and_populates_a_draft_release():
    workflow = WORKFLOWS / "prepare-release.yml"

    assert workflow.is_file(), "draft release preparation workflow is missing"

    contents = workflow.read_text(encoding="utf-8")
    assert "release-tag:" in contents
    assert "attestations: write" in contents
    assert "actions/attest@v4" in contents
    assert "Release $RELEASE_TAG must still be a draft" in contents
    assert "gh release upload" in contents


def test_published_release_verifies_immutable_attested_assets_before_pypi():
    contents = (WORKFLOWS / "release.yml").read_text(encoding="utf-8")

    assert "gh release upload" not in contents
    assert "isImmutable" in contents
    assert "gh attestation verify" in contents
    assert "pypa/gh-action-pypi-publish@release/v1" in contents
