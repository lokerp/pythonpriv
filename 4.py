import os
import re


def get_imports_dict(dir_path):
    imports = {'full': [], 'part': {}}
    py_files = []

    for dirpath, dirnames, filenames in os.walk(dir_path):
        py_files.extend([os.path.join(dirpath, file) for file in filenames if file.endswith(".py")])
    for file in py_files:
        f = None
        try:
            f = open(file, "r")
        except IOError:
            print("Ошибка про чтении файла. Проверьте их целостность.")
            exit()

        file_info = f.read()
        full_check = re.findall(r'(?:^|\n)import (\w+)', file_info)
        if (len(full_check) > 0):
            imports['full'].extend(full_check)

        part_check = re.findall(r'(?:^|\n)from (\w+) import ((?:\w(?:, ?)?)+)+', file_info)
        if (len(part_check) > 0):
            for i in part_check:
                imports['part'].setdefault(i[0], []).extend([i.strip() for i in i[1].split(',') if not i.isspace()])

        f.close()
    return imports


input_path = input("Введите путь до директории: ")
if not os.path.isdir(input_path):
    print("Данной директории не существует!")
    exit()

imports = get_imports_dict(input_path)

with open("imports.txt", "w") as f:
    f.writelines([f"import {i}\n" for i in imports['full']])
    f.writelines([f"from {key} import {', '.join(value)}\n" for key, value in imports['part'].items()])
