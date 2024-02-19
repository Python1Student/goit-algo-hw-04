from pathlib import Path
from colorama import Fore, Style

COLORS = (Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.LIGHTBLACK_EX)


def directory(path: str, depth: int = 0) -> None:
    directory_path = Path(path)

    for item in directory_path.iterdir():
        name = item.name
        print(COLORS[6] + '-' * depth + Style.RESET_ALL, end='')
        if item.is_dir():
            print(COLORS[1] + name)
            directory(item, depth + 1)
        else: 
            print(COLORS[3] + name)
        

directory('')