def show_phonebook(phonebook):
    from read_dict import read_file_to_dict
    from print_file import print_contacts
    list_of_contacts = sorted(read_file_to_dict(phonebook), key=lambda x: x['Фамилия'])
    print_contacts(list_of_contacts)
    print()
    return list_of_contacts
