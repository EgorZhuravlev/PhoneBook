
def choose_action(phonebook):
    while True:
        print('Что вы хотите сделать?')
        user_choice = input('1 - Импортировать данные\n2 - Найти контакт\n3 - Добавить контакт\n\
4 - Изменить контакт\n5 - Удалить контакт\n6 - Просмотреть все контакты\n0 - Выйти из приложения\n')
        print()
        if user_choice == '1':
            from import_file import import_data
            file_to_add = input('Введите название импортируемого файла: ')
            import_data(file_to_add, phonebook)
        elif user_choice == '2':
            from read_dict import read_file_to_dict
            from find import find_number
            contact_list = read_file_to_dict(phonebook)
            find_number(contact_list)
        elif user_choice == '3':
            from new_number import add_phone_number
            add_phone_number(phonebook)
        elif user_choice == '4':
            from change_file import change_phone_number
            change_phone_number(phonebook)
        elif user_choice == '5':
            from delete_file import delete_contact
            delete_contact(phonebook)
        elif user_choice == '6':
            from show_file import show_phonebook
            show_phonebook(phonebook)
        elif user_choice == '0':
            print('До свидания!')
            break
        else:
            print('Неправильно выбрана команда!')
            print()
            continue

if __name__ == '__main__':
    file = 'Phonebook.txt'
    choose_action(file)