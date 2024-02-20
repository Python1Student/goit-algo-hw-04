from constants import *

def parse_input(user_input: str) -> tuple:
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def read_file() -> dict:
    contacts = {}

    with open('contacts.txt', 'r') as file:
        lines = file.readlines()

    for line in lines:
        line = line.strip().split()

        contacts[line[0]] = line[1]

    return contacts


def add_contact(name: str, number: str) -> None:
    contacts = read_file()
    
    contacts[name] = number
    
    with open('contacts.txt', 'w') as file:
        for key, value in contacts.items():    
            file.write(f'{key} {value}\n')

    print(BOT + 'Successful!')
    

def read_contact(name: str = None) -> None:
    contacts = read_file()

    if not name:
        for key, value in contacts.items(): 
            print(f'{key} {value}')
        return

    if name not in contacts.keys():
        print(ERROR + 'Contact Not Found!')
        return
    
    print(BOT + f'{name} {contacts[name]}')