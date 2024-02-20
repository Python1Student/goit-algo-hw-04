from constants import *
from functions import parse_input, add_contact, read_contact


def main():
    print(BOT + 'Welcome to assistant Bot!')

    while True:
        user_input = input(Fore.GREEN + '>>> ' + Style.RESET_ALL)
        command, *args = parse_input(user_input) if user_input else (None,)

        if command in ('exit', 'close'):
            print(BOT + 'Good Bye!')
            break

        elif command == 'hello':
            print(BOT + 'How can I help you?')

        elif command in ('add', 'change'):
            if len(args) == 2:
                add_contact(*args)
            else:
                print(ERROR + 'Wrong Contact Details!')

        elif command == 'phone':
            if args:
                read_contact(args[0])
            else:
                print(ERROR + 'Missed Contact Details!')

        elif command == 'all':
            read_contact()

        else: print(ERROR + 'Invalid Command')

if __name__ == '__main__':
    main()