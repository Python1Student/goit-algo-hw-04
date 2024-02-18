from pathlib import Path
import sys

def total_selery(path: str) -> tuple:
    file_path = Path(path)
    if file_path.exists():
        with open(file_path, 'r') as file:
            salary = [int(num.split(',')[1].strip()) for num in file.readlines()]
    else:
        print('File Not Found')
        sys.exit()

    total = sum(salary)
    average = int(total / len(salary))

    return total, average

total, average = total_selery('Task_1/salary_file.txt')
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")