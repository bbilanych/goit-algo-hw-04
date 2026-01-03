from pathlib import Path

def total_salary(path: str) -> tuple[int, float]:
    file_path = Path(path)
    if file_path.exists():
        with open(file_path, encoding="utf-8") as f:
            lines = [el.strip().split(',') for el in f.readlines()]

            total = sum(float(salary) for _, salary in lines)
            average = total / len(lines) if lines else 0

            print(f"Загальна сума заробітної плати: {total:.0f}, Середня заробітна плата: {average:.0f}")


# total, average = total_salary("path/to/salary_file.txt")

total_salary("salary.txt")