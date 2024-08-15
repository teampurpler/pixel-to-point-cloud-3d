from pathlib import Path
from typing import Optional

from git import Repo


def get_repo_path() -> Path:
    repo = Repo(".", search_parent_directories=True)
    return Path(repo.git.rev_parse("--show-toplevel"))


def get_all_files(
    changed_only: bool = False,
    extension: Optional[str] = None,
    compare_to_main: bool = False,
) -> list[Path]:
    repo_path = get_repo_path()
    repo = Repo(repo_path)
    files = []

    if changed_only:
        if compare_to_main:
            diff = repo.git.diff("main...HEAD", name_only=True).split("\n")
            files = [Path(repo_path, file) for file in diff if file]
        else:
            changed_files = [
                item.a_path for item in repo.index.diff(None)
            ] + repo.untracked_files
            files = [Path(repo_path, file) for file in changed_files]
    else:
        for blob in repo.tree().traverse():
            if blob.type == "blob":  # type: ignore
                files.append(Path(repo_path, blob.path))  # type: ignore

    if extension is not None:
        files = [file for file in files if file.suffix == extension]

    return files
