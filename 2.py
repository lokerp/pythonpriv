import os
import shutil


def get_files_size(dir_path):
    size = 0
    for dirpath, dirnames, filenames in os.walk(dir_path):
        for file in filenames:
            file_path = os.path.join(dirpath, file)
            file_size = os.path.getsize(file_path)
            size += file_size
            print(f"Файл: {file_path} | Размер {file_size} байт")
    return size


input_path = input("Введите путь до заархивированной директории (с расширением): ")
temp_dir = "unpacked"

if not os.path.isfile(input_path):
    print("Ошибка. Данной директории не существует.")
    exit()

try:
    shutil.unpack_archive(input_path, extract_dir=temp_dir)
except ValueError:
    print("Ошибка при распаковке архива. Проверьте, ведет ли путь к архиву.")
    exit()

common_size = get_files_size(temp_dir)
print(f"Общий размер архива: {common_size} байт")

shutil.rmtree(temp_dir)
