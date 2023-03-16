def read_file_to_list(phonebook):
    with open(phonebook, 'r', encoding='utf-8') as file:
        contact_list = []
        for line in file.readlines():
            contact_list.append(line.split())
    return contact_list