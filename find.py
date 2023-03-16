def find_number(contact_list):
    from search import search_parameters
    from print_file import print_contacts
    search_field, search_value  = search_parameters()
    search_value_dict = {'1': 'Surname', '2': 'Name', '3': 'Number'}
    found_contacts = []
    for contact in contact_list:
        if contact[search_value_dict[search_field]] == search_value:
            found_contacts.append(contact)
    if len(found_contacts) == 0:
        print('Контакт не найден!')
    else:
        print_contacts(found_contacts)
    print()