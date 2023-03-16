import os


def get_files_with_extension(dir_path, extension):
    files = []
    for dirpaths, dirnames, filenames in os.walk(dir_path):
        files.extend(file for file in filenames if file.endswith("." + extension))

    return files


path = input("Введите путь до директории: ")
ext = input("Введите имя расширения (без .): ")

if not os.path.isdir(path):
    print("Данной директории не существует!")
    exit()

print(get_files_with_extension(path, ext))
