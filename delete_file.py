def delete_contact(phonebook):
    from read_list import read_file_to_list
    from modify_search import search_to_modify
    contact_list = read_file_to_list(phonebook)
    number_to_change = search_to_modify(contact_list)
    contact_list.remove(number_to_change)
    with open(phonebook, 'w', encoding='utf-8') as file:
        for contact in contact_list:
            line = ' '.join(contact) + '\n'
            file.write(line)
