from pathlib import Path
from colorama import Fore, Style
from sys import argv

# Створюємо функцію для виводу вимісту директорії
def directory(path: str = '', depth: int = 1, is_root: bool = False) -> None:
    # Створюємо об'єкт Path
    directory_path = Path(path)
    # Перевіряємо чи функція викликається вперше
    if is_root:
        print('📦 ' + Fore.RED + directory_path.name + Style.RESET_ALL)

    # Перебираємо всі папки та файли
    for item in directory_path.iterdir():
        # Отримуємо імя файлу
        name = item.name
        # Виводимо отступи
        print(Fore.LIGHTBLACK_EX + '-' * depth + Style.RESET_ALL, end='')
        # Перевіряємо чи є обєкт папкой шоб ще раз відкрити
        if item.is_dir():
            # Виводимо
            print('📂 ' + Fore.GREEN + name + Style.RESET_ALL)
            # Викликаємо функцію рекурсивно
            directory(item, depth + 1)
        else: 
            # Якшо файл то виводимо
            print('📜 ' + Fore.BLUE + name + Style.RESET_ALL)

# Перевіряємо чи передали аргумент чи ні
if len(argv) > 1:
    directory(argv[1], is_root=True)
else: 
    directory(is_root=True)