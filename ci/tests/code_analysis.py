import argparse
from pathlib import Path

from ci_tools.code_analysis.flake8 import run_flake8
from ci_tools.code_analysis.formatting import run_formatting
from ci_tools.code_analysis.mypy import run_mypy
from ci_tools.code_analysis.pylint import run_pylint
from ci_tools.code_analysis.pyright import run_pyright
from ci_tools.repo import get_all_files

TYPES = ("formatting", "flake8", "mypy", "pyright", "pylint")


def _args() -> argparse.Namespace:
    all_types = ("all",) + TYPES
    parser = argparse.ArgumentParser(description="Code analysis")
    parser.add_argument(
        "type",
        type=str,
        choices=all_types,
        nargs="?",
        help=f"Type of code analysis to perform. Options: {all_types}",
        default="all",
    )
    parser.add_argument(
        "--fix",
        action="store_true",
        help="Automatically fix issues when possible.",
        required=False,
        default=False,
    )
    parser.add_argument(
        "--changed-only",
        action="store_true",
        help="Only analyze files that have changed in the current branch.",
        required=False,
        default=False,
    )
    parser.add_argument(
        "--compare-to-main",
        action="store_true",
        help="Compare the current branch to the main branch.",
        required=False,
        default=False,
    )
    parser.add_argument(
        "--paths",
        nargs="+",
        help="Paths to files or directories to analyze. If not provided, all files in the repository will be analyzed.",
        required=False,
        default=None,
    )
    return parser.parse_args()


def _run_code_analysis(type_: str, paths: list[Path], fix: bool = False) -> bool:
    match type_:
        case "flake8":
            return run_flake8(paths=paths)
        case "formatting":
            return run_formatting(paths=paths, check_only=not fix)
        case "mypy":
            return run_mypy(paths=paths)
        case "pylint":
            return run_pylint(paths=paths)
        case "pyright":
            return run_pyright(paths=paths)
        case _:
            raise ValueError(f"Invalid type: {type_}")


def _main() -> None:
    args = _args()
    paths = (
        get_all_files(
            changed_only=args.changed_only,
            extension=".py",
            compare_to_main=args.compare_to_main,
        )
        if args.paths is None
        else args.paths
    )
    types = TYPES if args.type == "all" else (args.type,)
    results = [
        _run_code_analysis(type_=type_, paths=paths, fix=args.fix) for type_ in types
    ]

    print("Code analysis results:")
    for type_, result in zip(types, results):
        print(f"    {type_}: {'Success' if result else 'Failure'}")

    assert all(results)


if __name__ == "__main__":
    _main()
