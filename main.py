import csv
import script as s


def main(path_initial_file, path_final_file):
    with open(path_initial_file, encoding='utf-8') as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)
    s.change_number(contacts_list)
    s.change_name(contacts_list)
    with open(path_final_file, "w", encoding='utf-8') as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(s.create_persons_list(contacts_list))
    print("\nВозможно, всё получилось.")


if __name__ == '__main__':
    initial_file = 'phonebook_raw.csv'
    final_file = 'phonebook.csv'
    main(initial_file, final_file)
