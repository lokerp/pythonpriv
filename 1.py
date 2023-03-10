import json

animals = None
birds = None
diurnal_animals = None
lighter_animal = None

try:
    with open("animals.json", "r") as file:
        animals_file = file.read()
except FileNotFoundError:
    print("Ошибка! Файл не найден!")
    exit()

try:
    animals = json.loads(animals_file)
except json.decoder.JSONDecodeError:
    print("Ошибка! Файл некорректного формата!")
    exit()

try:
    birds = list(filter(lambda x: x["animal_type"] == "Bird", animals["animals"]))
    diurnal_animals = len(list(filter(lambda x: x["active_time"] == "Diurnal", animals["animals"])))
    lighter_animal = min(animals["animals"], key=lambda x: float(x["weight_min"]))
except KeyError:
    print("Ошибка! В json файле отстутствует требуемые поля")

print(birds)
print(diurnal_animals)
print(lighter_animal)
