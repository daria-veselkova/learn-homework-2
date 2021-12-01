"""

Домашнее задание №2

Работа csv

1. Создайте список словарей с ключами name, age и job и значениями по вашему выбору. 
   В списке нужно создать не менее 4-х словарей
2. Запишите содержимое списка словарей в файл в формате csv

"""
import csv


persons = [
    {'name': 'Igor', 'age': 34, 'job': 'developer'},
    {'name': 'Rita', 'age': 27, 'job': 'anthropologist'},
    {'name': 'Lisa', 'age': 29, 'job': 'algologist'},
    {'name': 'Nick', 'age': 33, 'job': 'algologist'},
    {'name': "Ann", 'age': 42, 'job': 'teacher'},
    {'name': 'Hugh', 'age': 53, 'job': 'actor'},
    {'name': 'Elizabeth', 'age': 95, 'job': 'queen'},
    {'name': 'Jean-Luc', 'age': 65, 'job': 'captain'},
    {'name': 'Luke', 'age': 53, 'job': 'jedi'},
    ]


def main():
    with open('export.csv', 'w', encoding='utf-8', newline='') as export_file:
        fields = ['name', 'age', 'job']
        writer = csv.DictWriter(export_file, fields, delimiter=';')
        writer.writeheader()

        for person in persons:
            writer.writerow(person)

if __name__ == "__main__":
    main()
