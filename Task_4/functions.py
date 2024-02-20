from constants import *

# ЗАВДАННЯ
# Логіка команд реалізована в окремих функціях і ці функції приймають на вхід один або декілька рядків та повертають рядок.

# Функція для парсингу данних
def parse_input(user_input: str) -> tuple:
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

# Читаємо файл з контактами
def read_file() -> dict:
    contacts = {}

    # Читаємо файл
    with open('contacts.txt', 'r') as file:
        # Робимо список зі строк
        lines = file.readlines()
    
    # Парсимо строку
    for line in lines:
        line = line.strip().split()

        # Додаємо строку до словника
        contacts[line[0]] = line[1]

    # Повертаємо словник
    return contacts


# Функція для додавання та модифікації словника
def add_contact(name: str, number: str) -> str:
    # Читаємо файл та присвоюємо його значення в словник
    contacts = read_file()
    
    # Додаємо наш контакт до словника або замінюємо якщо є
    contacts[name] = number
    
    # Записуємо словник в файл
    with open('contacts.txt', 'w') as file:
        for key, value in contacts.items():    
            file.write(f'{key} {value}\n')

    # Повертаємо успішне виконання
    return BOT + 'Successful!'
    

# Функція Для читання контактів
def read_contact(name: str = None) -> str:
    # Читаємо файл та присвоюємо його значення в словник
    contacts = read_file()

    # Перевіряємо чи пустий файл
    if not contacts:
        return ERROR + 'Not Contacts!'

    # Перевіряємо чи шукаємо ми один контакт чи всі
    if not name:
        text = BOT + 'Contacts:\n'
        for key, value in contacts.items(): 
            text += f'{key} {value}'
            if key != list(contacts.keys())[-1]: text += '\n'
        return text

    # Перевіряємо чи яке імя шукаємо в файлі
    if name not in contacts.keys():
        return ERROR + 'Contact Not Found!'
    
    # Повертаємо імя яке шукали
    return BOT + f'{name} {contacts[name]}'