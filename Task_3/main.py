from pathlib import Path

def directory(path: str) -> None:
    directory_path = Path(path)

    for i in directory_path.iterdir():
        if i.is_dir():
            directory(i)
        else: print(i)

directory('')