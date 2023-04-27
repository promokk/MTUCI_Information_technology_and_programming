# import numpy as np
# import pandas as pd

from statistics import mean
from operator import itemgetter, attrgetter


groupmates = [
    {
        "name": "Александр",
        "surname": "Иванов",
        "exams": ["Информатика", "ЭЭиС", "Web"],
        "marks": [4, 3, 5]
    },
    {
        "name": "Иван",
        "surname": "Петров",
        "exams": ["История", "АиГ", "КТП"],
        "marks": [4, 4, 4]
    },
    {
        "name": "Алена",
        "surname": "Смирнова",
        "exams": ["Философия", "ИС", "КТП"],
        "marks": [5, 5, 5]
    },
    {
        "name": "Петр",
        "surname": "Попов",
        "exams": ["Философия", "ИС", "КТП"],
        "marks": [5, 3, 3]
    },
    {
        "name": "Кирилл",
        "surname": "Смирнов",
        "exams": ["Философия", "АиГ", "Web"],
        "marks": [3, 4, 4]
    }
]

def print_students(students, score):
    # students = sorted(students, key=lambda d: mean(d['marks']))
    print(u"Имя".ljust(15), u"Фамилия".ljust(10), u"Экзамены".ljust(30), u"Средная оценка".ljust(20))
    for student in students:
        if (mean(student["marks"]) >= score):
            print(student["name"].ljust(15), student["surname"].ljust(10), str(student["exams"]).ljust(30), str(round(mean(student["marks"]), 2)).ljust(20))

print_students(groupmates, 4)
