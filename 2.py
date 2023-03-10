import csv

file = None
csv_reader = None
income_range = None

try:
    file = open("countries.csv", "r")
except FileNotFoundError:
    print("Ошибка! Файл не найден!")
    exit()

try:
    csv_reader = csv.reader(file, dialect=csv.excel)
except csv.Error:
    print("Ошибка! Файл некорректного формата!")
    exit()

try:
    income_range = list(map(lambda x: float(x), input("Введите диапазон доходов через пробел: ").split(' ')))
    if len(income_range) != 2 or income_range[0] > income_range[1]:
        raise ValueError
except ValueError:
    print("Ошибка! Введено неверное значение!")
    exit()

csv_reader_list = list(csv_reader)

new_file = open("income_sorted_countries.csv", mode="w+", newline='')
csv_writer = csv.writer(new_file, dialect=csv.excel, quoting=csv.QUOTE_NONNUMERIC)
csv_writer.writerow(csv_reader_list[0])
csv_writer.writerows(list(filter(lambda x: income_range[0] <= float(x[2]) <= income_range[1], csv_reader_list[1:])))
new_file.close()

new_file = open("inflation_sorted_countries.csv", mode="w+", newline='')
csv_writer = csv.writer(new_file, dialect=csv.excel, quoting=csv.QUOTE_NONNUMERIC)
csv_writer.writerow(csv_reader_list[0])
csv_writer.writerows(sorted(csv_reader_list[1:], key=lambda x: float(x[3])))
new_file.close()

file.close()
