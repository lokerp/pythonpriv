import json

animals = None
birds = None
diurnal_animals = None
lighter_animal = None

try:
    with open("animals.json", "r") as file:
        animals_json = file.read()
except FileNotFoundError:
    print("Ошибка! Файл не найден!")
    exit()

try:
    animals = json.loads(animals_json)
except json.decoder.JSONDecodeError:
    print("Ошибка! Файл некорректного формата!")
    exit()

try:
    birds = [i for i in animals["animals"] if i["animal_type"] == "Bird"]
    diurnal_animals = len([i for i in animals["animals"] if i["active_time"] == "Diurnal"])
    lighter_animal = min(animals["animals"], key=lambda x: float(x["weight_min"]))
except KeyError:
    print("Ошибка! В json файле отстутствует требуемые поля")

print(birds)
print(diurnal_animals)
print(lighter_animal)

