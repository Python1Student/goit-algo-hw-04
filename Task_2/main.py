from pathlib import Path
from sys import exit


# Створюємо функцію для обробки данних
def get_cats_info(path: str) -> list:
    # Створюємо об'єкт Path
    file_path = Path(path)
    # Створюємо список в який будемо додавати словники
    cats_info = []

    # Перевіряємо чи існує файл
    if file_path.exists():
        # Відкриваємо файл
        with open(file_path, 'r', encoding='utf-8') as file:
            # Робимо список списків данних з файлу
            cats_list = [line.strip().split(',') for line in file.readlines()]
    # Якщо файл не знайдено то завершуємо програму і виводимо помилку
    else:         
        exit('File Not Found')

    # Робимо та додаємо словники в список
    for cat in cats_list:
        # Робимо новий словник кожного разу шоб не повторювалися
        cats_dict = {
            'id'  : cat[0],
            'name': cat[1],
            'age' : cat[2]
        }
        # Додаємо словник в список
        cats_info.append(cats_dict)

    # Повертаємо список
    return cats_info

# Присвоюєм результат функції
cats_info = get_cats_info('Task_2/cats_file.txt')
# Виводимо результат
for cat in cats_info:
    print(cat)