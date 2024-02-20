from colorama import Fore, Style

BOT   = Fore.CYAN + '[BOT] ' + Style.RESET_ALL
ERROR = Fore.RED + '[ERROR] ' + Style.RESET_ALL

def main():
    print(BOT + 'Welcome to assistant Bot!')

    while True:
        command = input(Fore.GREEN + '>>> ' + Style.RESET_ALL).strip().lower()

        if command in ('exit', 'close'):
            print(BOT + 'Good Bye!')
            break

        elif command == 'hello':
            print(BOT + 'How can I help you?')

        else: print(ERROR + 'Invalid Command')

if __name__ == '__main__':
    main()