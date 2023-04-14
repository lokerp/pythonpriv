import csv
import datetime
from docxtpl import DocxTemplate

file = None
reader = None
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
winners = []
winners_list = list(reader)
winners_list.sort(key=lambda x: x.get('Year'))
for i in range(len(winners_list)):
    year_first = winners_list[i].get('Year')
    city_first = winners_list[i].get('City')
    dic = {'Year': year_first,
           'City': city_first,
           'Winner': [{winners_list[i][k] for k in range(1, 4)}]}
    for j in range(len(winners_list) + 1):
        year_second = winners_list[j].get('Year')
        city_second = winners_list[j].get('City')
        if year_first == year_second and city_first == city_second:
            dic.get('Winner').append({winners_list[j][k] for k in range(1, 4)})
            winners_list.pop(j)
    winners.append(dic)
print(winners)

print(winners_list)
for i in range(len(winners_list)):
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
    this_year = winners_list[i].get('Year')
    this_time = None
    try:
        this_time = datetime.datetime.strptime(winners_list[i].get('Time'), '%m/%d/%y %H:%M:%S')
    except ValueError:
        pass
    context['year'] = this_year
    context['city'] = winners_list[i].get('City')
    this_sex = winners_list[i].get('Sex')
    this_name = winners_list[i].get('Name')
    if this_sex == "Male":
        context['male_name'] = this_name
        if this_time is not None:
            context['male_time'] = winners_list[i].get('Time')
    elif this_sex == "Female":
        context['female_name'] = this_name
        if this_time is not None:
            context['female_time'] = winners_list[i].get('Time')

    if i < len(winners_list) - 1:
        next_time = None
        try:
            next_time = datetime.datetime.strptime(winners_list[i + 1].get('Time'), '%H:%M:%S')
        except ValueError:
            pass
        next_sex = winners_list[i + 1].get('Sex')
        next_name = winners_list[i + 1].get('Name')
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
