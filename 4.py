import numpy as np
from enum import Enum

class Levels(Enum):
    Beginner = 0
    Intermediate = 1
    Expert = 2
    All = 3
    
def str_to_enum(lvl):
    lvl = lvl.decode("utf-8")
    match lvl:
        case 'Beginner Level':
            return Levels.Beginner.value
        case 'Intermediate Level':
            return Levels.Intermediate.value
        case 'Expert Level':
            return Levels.Expert.value
        case 'All Levels':
            return Levels.All.value

conv = {
    4: str_to_enum
}
data = np.loadtxt('udemy_courses.csv', delimiter=',', skiprows=1, converters=conv, usecols=range(1, 6))

cost_mean = data.mean(axis=0)[0]
print(f"Средняя цена за курс: {cost_mean}")

subs_min = data.min(axis=0)[1]
print(f"Минимальное количество подписчиков: {subs_min}")

length_max = data.max(axis=0)[-1]
print(f"Максимальная продолжительность лекций: {length_max}")

unique, counts = np.unique(data[:, 3], return_counts=True)
max_count_lvl = unique[np.argmax(counts)]
print(f"Уровень, для которого было создано наибольшее количество курсов: {Levels(max_count_lvl).name}")