from __future__ import annotations

import sys
from pathlib import Path
from typing import Iterable

try:
    from colorama import Fore, Style, init as colorama_init
except ImportError as e:

    print("Error: 'colorama' is not installed.\n"
          "Create/activate your virtual environment and run: pip install colorama",
          file=sys.stderr)
    raise


def iter_sorted_entries(path: Path) -> Iterable[Path]:
    try:
        entries = list(path.iterdir())
    except PermissionError:
        print(f"{Fore.RED}Permission denied: {path}{Style.RESET_ALL}")
        return []
    except OSError as e:
        print(f"{Fore.RED}OS error accessing {path}: {e}{Style.RESET_ALL}")
        return []

    entries.sort(key=lambda p: (p.is_file(), p.name.lower()))
    return entries


def print_tree(root: Path, prefix: str = "") -> None:
    entries = list(iter_sorted_entries(root))
    count = len(entries)
    for idx, entry in enumerate(entries):
        connector = "└── " if idx == count - 1 else "├── "
        next_prefix = prefix + ("    " if idx == count - 1 else "│   ")

        if entry.is_dir():
            print(f"{prefix}{connector}{Fore.CYAN}{entry.name}{Style.RESET_ALL}")
            print_tree(entry, next_prefix)
        elif entry.is_file():
            print(f"{prefix}{connector}{Fore.GREEN}{entry.name}{Style.RESET_ALL}")
        else:
            # Symlinks or special files
            print(f"{prefix}{connector}{Fore.YELLOW}{entry.name}{Style.RESET_ALL}")


def main(argv: list[str]) -> int:
    colorama_init(autoreset=True)

    if len(argv) < 2:
        print("Usage: python hw03.py <path-to-directory>", file=sys.stderr)
        return 2

    target = Path(argv[1]).expanduser().resolve()

    if not target.exists():
        print(f"{Fore.RED}Error: path does not exist: {target}{Style.RESET_ALL}", file=sys.stderr)
        return 1
    if not target.is_dir():
        print(f"{Fore.RED}Error: path is not a directory: {target}{Style.RESET_ALL}", file=sys.stderr)
        return 1

    # Print the root directory name first
    print(f"{Fore.CYAN}{target.name}{Style.RESET_ALL}")
    print_tree(target)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
