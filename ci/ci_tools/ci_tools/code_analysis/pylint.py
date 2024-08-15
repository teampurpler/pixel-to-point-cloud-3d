import subprocess
from pathlib import Path

from ci_tools.repo import get_all_files


def _get_config_path() -> Path:
    return Path(__file__).parent / "configurations"


def run_pylint(paths: list[Path]) -> bool:
    config_file = _get_config_path() / ".pylintrc"
    return (
        subprocess.run(
            [
                "pylint",
                "--rcfile",
                str(config_file),
                *paths,
            ],
            check=False,
        ).returncode
        == 0
    )


if __name__ == "__main__":
    paths_ = get_all_files(extension=".py")
    assert run_pylint(paths=paths_)
