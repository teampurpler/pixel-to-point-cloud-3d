import subprocess
from pathlib import Path

from ci_tools.repo import get_all_files


def run_pyright(paths: list[Path]) -> bool:
    return (
        subprocess.run(
            [
                "pyright",
                *paths,
            ],
            check=False,
        ).returncode
        == 0
    )


if __name__ == "__main__":
    paths_ = get_all_files(extension=".py")
    assert run_pyright(paths=paths_)
