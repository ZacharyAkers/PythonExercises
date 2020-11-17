import pickle
with open('contact.pickle', 'rb') as fh:
    data = pickle.load(fh)

def welcome():
    entry = int(input("""Welcome to the Electronic Phone Book.\n What would you like to do?\n 1. Look up a entry.\n 2. Set an entry.\n 3. Delete an entry.\n 4. List all entries.\n 5. Quit\n Please enter a entry(1-5) """))
    return entry

def phonebook():
    contact = {}
    while True:
        entry = welcome()
        if entry == 1:
            name = input("Name of who you are trying to look up ")
            if name in contact:
                print("The contact is ", name, ':', contact[name])
            elif data:
                print("The contact is ", data)
            else:
                print("That contact doesnt exist. Return to main list to enter the contact")

        elif entry == 2:
            phone_number = input('Please put your phone number: ')
            contact_name = input('Please put your name: ')
            if phone_number not in contact.items():
                contact.update({contact_name:phone_number})
                print("Contact successfully saved")
                print("Your updated contact book is shown below")
                for k, v in contact.items():
                    print(k, '', v)
            else:
                print("That Contact is already in your Phonebook")

        elif entry == 3:
            name = input("Enter the name of the contact you wish to delete ")
            if name in contact:
                print('The contact is ', name, ":", contact[name])
            elif data:
                print("The contact is ", data)
            else:
                print('That name does not exist')
            confirm = input('Are you sure you wish to delete this contact? Yes/No ')
            if confirm == 'Yes':
                contact.pop(name, None)
                for k, v in contact.items():
                    print("Your update list is shown below")
                    print(k, '', v)
            else:
                print("Return to main menu")

        elif entry == 4:
            if bool(contact) != False:
                for k, v in contact.items():
                    print(k, '', v)
            else:
                print('You have a empty phonebok')

        elif entry == 5:
            print('Thanks for using Virtual Phonebook')
            with open('contact.pickle', 'wb') as fh:
                pickle.dump(contact, fh)
            break

        else:
            print("Invalid option")
print(phonebook())


