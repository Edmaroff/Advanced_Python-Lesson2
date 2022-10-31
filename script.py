import re


# Создание 2ух словарей: уникальных строк и дубликатов, ключи ФИ
def create_dict_person(contacts_list):
    unique_persons = {}
    duplicate_person = {}
    for data in contacts_list[1:]:
        if unique_persons.get(' '.join(data[0:2])) is None:
            unique_persons[' '.join(data[0:2])] = data[2:]
        else:
            duplicate_person[' '.join(data[0:2])] = data[2:]
    return [unique_persons, duplicate_person]


# Перенос информации из словаря дубликатов в уникальный
def remove_duplicates(contacts_list):
    unique_persons, duplicate_person = create_dict_person(contacts_list)
    for dup_name_person, dup_data_person in duplicate_person.items():
        for i, un_data_person in enumerate(unique_persons[dup_name_person]):
            if un_data_person == '':
                unique_persons[dup_name_person][i] = dup_data_person[i]
    return unique_persons


# Добавление ФИ в значения словаря уникальных строк
def add_person_name(contacts_list):
    unique_persons = remove_duplicates(contacts_list)
    for un_name_person, un_data_person in unique_persons.items():
        str_name_person = (''.join(un_name_person)).split()
        un_data_person.insert(0, str_name_person[0])
        un_data_person.insert(1, str_name_person[1])
    return unique_persons


# Создание списка из словаря уникальных строк, пригодного к записи в csv файл
def create_persons_list(contacts_list):
    unique_persons = add_person_name(contacts_list)
    persons_list = [contacts_list[0]]
    for data in unique_persons.values():
        persons_list.append(data)
    return persons_list


# Изменение формата номера телефона на: +7(999)999-99-99 доб.9999
def change_number(contacts_list):
    pattern_main_number = r'(\+7|8)\W*(\d{3})\W*(\d{3})\W*(\d{2})\W*(\d{2})'
    pattern_additional_number = r'\(?\w{3}[\s.]+(\d{4})\)?'
    replacement_main = r'+7(\2)\3-\4-\5'
    replacement_additional = r'доб.\1'
    for row in contacts_list:
        row[-2] = re.sub(pattern_main_number, replacement_main, row[-2])
        row[-2] = re.sub(pattern_additional_number, replacement_additional, row[-2])


# Изменение формата ФИО на: Ф,И,О
def change_name(contacts_list):
    for row in contacts_list:
        full_name = ' '.join(row[0:3]).strip().split(' ')
        row[:3] = full_name + [''] * (3 - len(full_name))
