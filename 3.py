import os
import shutil


def move_files(src, dst, ext):
    for dirpath, dirnames, filenames in os.walk(src):
        for file in filenames:
            for ext in ext_to_copy:
                if file.endswith("." + ext):
                    shutil.move(os.path.join(dirpath, file), dst)


ext_to_copy = ["jpg", "png"]

src = input("Введите путь исходной директории: ")
if not os.path.isdir(src):
    print("Данной директории не существует!")
    exit()

dst = input("Введите путь директории для копирования: ")
if not os.path.isdir(dst):
    print("Данной директории не существует!")
    exit()

move_files(src, dst, ext_to_copy)
shutil.make_archive(dst, "zip", base_dir=dst)
