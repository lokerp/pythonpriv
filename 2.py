import csv
import datetime
from docxtpl import DocxTemplate

file = None
reader = None
page_break_sym = "\f"
pages = []

doc_tmp = DocxTemplate("winners_doc_template.docx")

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
reader_list.sort(key=lambda x: x.get('Year'))

print(reader_list)
for i in range(len(reader_list)):
    page_tmp = DocxTemplate("winners_page_template.docx")
    context = {
        "year": None,
        "city": None,
        "male_name": None,
        "male_time": None,
        "female_name": None,
        "female_time": None,
        "page_break": ""
    }
    this_year = reader_list[i].get('Year')
    this_time = None
    try:
        this_time = datetime.datetime.strptime(reader_list[i].get('Time'), '%m/%d/%y %H:%M:%S')
    except ValueError:
        pass
    context['year'] = this_year
    context['city'] = reader_list[i].get('City')
    this_sex = reader_list[i].get('Sex')
    this_name = reader_list[i].get('Name')
    if this_sex == "Male":
        context['male_name'] = this_name
        if this_time is not None:
            context['male_time'] = reader_list[i].get('Time')
    elif this_sex == "Female":
        context['female_name'] = this_name
        if this_time is not None:
            context['female_time'] = reader_list[i].get('Time')

    if i < len(reader_list) - 1:
        next_time = None
        try:
            next_time = datetime.datetime.strptime(reader_list[i + 1].get('Time'), '%H:%M:%S')
        except ValueError:
            pass
        next_sex = reader_list[i + 1].get('Sex')
        next_name = reader_list[i + 1].get('Name')
        if this_time is not None and next_time is not None:
            if this_sex == next_sex and this_time <= next_time:
                continue
        if next_sex == "Male":
            context['male_name'] = next_name
            if next_time is not None:
                context['male_time'] = next_time.strftime('%H:%M:%S')
        elif next_sex == "Female":
            context['female_name'] = next_name
            if next_time is not None:
                context['male_time'] = next_time.strftime('%H:%M:%S')
        context['page_break'] = page_break_sym

    page_tmp.render(context)

    sub_tmp = doc_tmp.new_subdoc()
    sub_tmp.subdocx = page_tmp.docx

    pages.append(sub_tmp)


context = {"pages": pages}
doc_tmp.render(context)
doc_tmp.save("winners.docx")
