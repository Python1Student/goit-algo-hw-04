from pathlib import Path
from sys import exit


def get_cats_info(path: str) -> list:
    file_path = Path(path)
    cats_info = []

    if file_path.exists():
        with open(file_path, 'r', encoding='utf-8') as file:
            cats_list = [line.strip().split(',') for line in file.readlines()]
    else:         
        exit('File Not Found')

    for cat in cats_list:
        cats_dict = {}
        cats_dict['id'], cats_dict['name'], cats_dict['age'] = cat
        cats_info.append(cats_dict)

    return cats_info


cats_info = get_cats_info('Task_2/cats_file.txt')
for cat in cats_info:
    print(cat)