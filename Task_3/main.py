from pathlib import Path
from colorama import Fore, Style
from sys import argv

COLORS = (Fore.GREEN, Fore.BLUE, Fore.LIGHTBLACK_EX, Fore.RED)


def directory(path: str = '', depth: int = 1, is_root: bool = False) -> None:
    directory_path = Path(path)
    if is_root:
        print('📦 ' + COLORS[-1] + directory_path.name + Style.RESET_ALL)

    for item in directory_path.iterdir():
        name = item.name
        print(COLORS[2] + '-' * depth + Style.RESET_ALL, end='')
        if item.is_dir():
            print('📂 ' + COLORS[0] + name + Style.RESET_ALL)
            directory(item, depth + 1)
        else: 
            print('📜 ' + COLORS[1] + name + Style.RESET_ALL)
        
if len(argv) > 1:
    directory(argv[1], is_root=True)
else: 
    directory(is_root=True)