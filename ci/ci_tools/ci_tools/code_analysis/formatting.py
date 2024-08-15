import subprocess
from pathlib import Path

from ci_tools.repo import get_all_files


def _get_config_path() -> Path:
    return Path(__file__).parent / "configurations"


def _read_text_config(path: Path) -> list[str]:
    with path.open() as file:
        return [line.strip() for line in file.readlines()]


def _run_black(paths: list[Path], check_only: bool = False) -> int:
    options = _read_text_config(_get_config_path() / ".black")
    extra_options = ("--check", "--diff") if check_only else ()
    return subprocess.run(
        ["black", *options, *extra_options, *paths],
        check=False,
    ).returncode


def _run_isort(paths: list[Path], check_only: bool = False) -> int:
    options = _read_text_config(_get_config_path() / ".isort")
    extra_options = ("--check-only",) if check_only else ()
    return subprocess.run(
        [
            "isort",
            *options,
            *extra_options,
            *paths,
        ],
        check=False,
    ).returncode


def run_formatting(paths: list[Path], check_only: bool = False) -> bool:
    black = _run_black(paths, check_only)
    isort = _run_isort(paths, check_only)
    return (black == 0) and (isort == 0)


if __name__ == "__main__":
    paths_ = get_all_files(extension=".py")
    assert run_formatting(paths=paths_, check_only=True)
