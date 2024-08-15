from pathlib import Path

from ci_tools.repo import get_repo_path


def _get_vision3d_path() -> Path:
    return get_repo_path() / "vision3d"


def _get_all_vision3d_markdown_files() -> list[Path]:
    markdown_files = [get_repo_path() / "README"]

    paths = _get_vision3d_path().rglob("*.py")
    for path in paths:
        lines = path.read_text(encoding="utf-8").splitlines()
        if "# %% [markdown]" in lines:
            markdown_files.append(path.parent / path.stem)

    paths = _get_vision3d_path().rglob("*.md")
    for path in paths:
        markdown_files.append(path.parent / path.stem)

    return markdown_files


def _get_all_toc_markdown_files() -> list[Path]:
    toc_path = get_repo_path() / "_toc.yml"
    lines = toc_path.read_text(encoding="utf-8").splitlines()

    files = []
    for line in lines:
        if "root: " in line:
            files.append(get_repo_path() / line.strip()[6:])
        if "- file: " in line:
            files.append(get_repo_path() / line.strip()[8:])

    return files


def _get_all_ignores_book_files() -> list[Path]:
    vision3d_path = _get_vision3d_path()
    ignore_path = vision3d_path.parent / ".bookignore"
    with open(ignore_path, "r", encoding="utf-8") as file:
        lines = file.readlines()

    files = []
    for line in lines:
        globbed_files = vision3d_path.rglob(line.strip())
        for globbed_file in globbed_files:
            files.append(globbed_file.parent / globbed_file.stem)

    return files


def test_toc() -> None:
    markdown_files = _get_all_vision3d_markdown_files()
    toc_files = _get_all_toc_markdown_files()
    ignore_files = _get_all_ignores_book_files()

    # Check that all calibration markdown files are included in toc or ignored
    for markdown_file in markdown_files:
        if (markdown_file not in toc_files) and (markdown_file not in ignore_files):
            raise AssertionError(
                f"{markdown_file.relative_to(get_repo_path()).as_posix()} not found in _toc.yml or .bookignore"
            )

    # Check that all files in toc actually exist
    for toc_file in toc_files:
        if toc_file not in markdown_files:
            raise AssertionError(
                f"{toc_file.relative_to(get_repo_path()).as_posix()} does not exist, but is referenced in _toc.yml"
            )

    # Check that ignored file are not included in toc
    for ignore_file in ignore_files:
        if ignore_file in toc_files:
            raise AssertionError(
                f"{ignore_file.relative_to(get_repo_path()).as_posix()} exist in .bookignore, but is referenced in _toc.yml"
            )


if __name__ == "__main__":
    test_toc()
