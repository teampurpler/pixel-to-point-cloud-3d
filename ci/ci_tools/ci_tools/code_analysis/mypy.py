import subprocess
from pathlib import Path

from ci_tools.repo import get_all_files


def _get_config_path() -> Path:
    return Path(__file__).parent / "configurations"


def run_mypy(paths: list[Path]) -> bool:
    paths_clean = [path for path in paths if "setup.py" != path.name]
    config_file = _get_config_path() / ".mypy.ini"
    return (
        subprocess.run(
            [
                "mypy",
                "--config-file",
                str(config_file),
                *paths_clean,
            ],
            check=False,
        ).returncode
        == 0
    )


if __name__ == "__main__":
    paths_ = get_all_files(extension=".py")
    assert run_mypy(paths=paths_)
