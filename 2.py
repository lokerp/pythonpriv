import csv
from docxtpl import DocxTemplate

file = None
reader = None

template = DocxTemplate("winners.docx")

try:
    file = open("data_marathon.csv", "r")
except FileNotFoundError:
    print("Ошибка! Файл не найден!")
    exit()
    
fieldnames = ["Year", "Name", "Sex", "Country", "Time", "City"]
try:
    reader = csv.DictReader(file, fieldnames, dialect=csv.excel)
except csv.Error:
    print("Ошибка! Файл некорректного формата!")
    exit()

reader_list = list(reader)
print(reader_list)
