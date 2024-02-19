from pathlib import Path
from sys import exit

# Створюємо функцію для обробки данних
def total_selery(path: str) -> tuple:
    # Створюємо об'єкт Path
    file_path = Path(path)
    # Перевіряємо чи існує файл з данними
    if file_path.exists():
        # Відкриваємо файл
        with open(file_path, 'r', encoding='utf-8') as file:
            # Робимо список з зарплатами
            salary = [int(num.split(',')[1].strip()) for num in file.readlines()]
    # Якщо файла не існує виводимо це і закриваємо програму
    else:
        exit('File Not Found')

    # Робимо змінну з сумою
    total   = sum(salary)
    # Та змінну з середнім значенням
    average = int(total / len(salary))

    # Повертаємо результат
    return total, average

# Присвоюємо результат
total, average = total_selery('Task_1/salary_file.txt')
# Виводимо результат
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")