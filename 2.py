import csv
from docxtpl import DocxTemplate
import datetime

file = None
reader = None
# pages = []
winners = []
output_list = []

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

winners_list = sorted(list(reader), key=lambda x: x.get('Year'))
i, winners_list_len = 0, len(winners_list)
while winners_list_len:
    year_first = winners_list[i].get('Year')
    city_first = winners_list[i].get('City')
    dic = {'Year': year_first,
           'City': city_first,
           'Winners': sorted([dict(list(el.items())[1:5]) for el in winners_list if el.get('Year') == year_first and el.get('City') == city_first],
                             key=lambda x: datetime.datetime.strptime(x.get('Time'), '%H:%M:%S'), reverse=True)}
    winners.append(dic)
    winners_list = list(filter(lambda x: x.get('Year') != year_first or x.get('City') != city_first, winners_list))
    i, winners_list_len = 0, len(winners_list)

for i in winners:
    # page_tmp = DocxTemplate("winners_page_template.docx")
    context = {
        "year": i.get('Year'),
        "city": i.get('City'),
        "male_name": "Нет данных",
        "male_time": "Нет данных",
        "female_name": "Нет данных",
        "female_time": "Нет данных"
    }
    for j in i.get('Winners'):
        if j.get('Sex') == "Female":
            context["female_name"] = j.get("Name")
            context["female_time"] = j.get("Time")
        elif j.get("Sex") == "Male":
            context["male_name"] = j.get("Name")
            context["male_time"] = j.get("Time")
    output_list.append(f"Год:{context['year']}\n"
                       f"Город:{context['city']}\n"
                       f"Победитель-мужчина: {context['male_name']}. Время: {context['male_time']}\n"
                       f"Победитель-женщина: {context['female_name']}. Время: {context['female_time']}"
                       f"\f")
    # page_tmp.render(context)
    # sub_tmp = doc_tmp.new_subdoc()
    # sub_tmp.subdocx = page_tmp.docx
    #
    # pages.append(sub_tmp)

context = {"pages": output_list}
doc_tmp.render(context)
doc_tmp.save("winners.docx")
