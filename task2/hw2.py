from pathlib import Path
from typing import Any


def total_salary(path: str) -> list[dict[str, Any]] | None:
    file_path = Path(path)
    if file_path.exists():
        with open(file_path, encoding="utf-8") as f:
            lines = [el.strip().split(',') for el in f.readlines()]
            return [{"id": id, "name": name, "age": age} for id, name, age in lines]
    return None


print(total_salary("cats.txt"))