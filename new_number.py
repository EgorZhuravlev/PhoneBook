def get_new_number():
    last_name = input('Введите фамилию: ')
    first_name = input('Введите имя: ')
    phone_number = input('Введите номер телефона: ')
    return last_name, first_name, phone_number


def add_phone_number (phonebook):
    info = ' '.join(get_new_number())
    with open(phonebook, 'a', encoding='utf-8') as phonebook:
        phonebook.write(f'{info}\n')