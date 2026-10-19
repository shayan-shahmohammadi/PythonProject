import csv
import os

print("---------- WELCOME ------------")

CSV_file = "contacts.csv"

contacts = {
    "Shayan" : 9393324356 ,
    "Arshia" : 9383454565 ,
    "Bardia" : 9302348764
}


def load_contacts():

    if os.path.exists(CSV_file):
        with open(file = CSV_file , mode = "r" , newline = "" , encoding = "utf-8") as file:
            reader = csv.reader(file)
            next(reader, None)
            loaded = {}
            for row in reader:
                if len(row) == 2:
                    name ,phone = row
                    try:
                        loaded[name] = int(phone)
                    except ValueError:
                        continue

            if loaded:
                contacts.clear()
                contacts.update(loaded)


def save_contacts():

    with open(file = CSV_file , mode = "w" , newline = "" , encoding = "utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Name" , "Phone"])
        for name, phone in contacts.items():
            writer.writerow([name, phone])




class Contact:

    @staticmethod
    def add_contact():

        while True:
            name = input("Enter your name: ")
            if name.replace(" " , "").isalnum():

                if name not in contacts.keys():

                    while True:
                        phone = input("Enter your phone number: ")
                        if phone.isnumeric():
                            phone = int(phone)

                            if phone not in contacts.values():

                                len_phone = len(str(phone))
                                if len_phone == 10:

                                    contacts[name] = phone
                                    save_contacts()

                                    print("Contact added successfully")
                                    print(contacts)
                                    return


                                else:
                                    print("Invalid phone number")

                            else:
                                print("Phone number is already exist.")

                        else:
                            print("Invalid phone number")

                else:
                    print("Contact already exists")

            else:
                print("Invalid name...")



    @staticmethod
    def search_contact():

        while True:
            name = input("Enter your name: ")
            if name.replace(" " , "").isalnum():

                if name in contacts.keys():

                    while True:
                        phone = input("Enter your phone number: ")
                        if phone.isnumeric():
                            phone = int(phone)

                            len_phone = len(str(phone))
                            if len_phone == 10:

                                if phone in contacts.values():

                                    print(f"{name} : {phone} has found!")
                                    return

                                else:
                                    print("Contact does not exist")

                            else:
                                print("Invalid phone number")

                        else:
                            print("Invalid phone number")

                else:
                    print("Contact does not exist")

            else:
                print("Invalid name...")


    @staticmethod
    def edit_contact():

        while True:
            name = input("Enter the name you want to edit: ")
            if name.replace(" " , "").isalnum():

                if name in contacts.keys():

                    while True:
                        phone = input("Enter the phone you want to edit: ")
                        if phone.isnumeric():
                            phone = int(phone)

                            len_phone = len(str(phone))
                            if len_phone == 10:

                                if phone in contacts.values():

                                    while True:
                                        new_name = input("Enter your new name: ")
                                        if new_name.replace(" " , "").isalnum():

                                            while True:
                                                new_phone = input("Enter your new phone number: ")
                                                if new_phone.isnumeric():
                                                    new_phone = int(new_phone)

                                                    len_new_phone = len(str(new_phone))
                                                    if len_new_phone == 10:

                                                       del contacts[name]
                                                       contacts[new_name] = new_phone
                                                       save_contacts()

                                                       print(f"{name} : {phone} had changed to {new_name} : {new_phone}")
                                                       print(contacts)
                                                       return

                                                    else:
                                                        print("Invalid phone number")

                                                else:
                                                    print("Invalid phone number")

                                        else:
                                            print("Invalid contact name")

                                else:
                                    print("Contact does not exist")

                            else:
                                print("Invalid phone number")

                        else:
                            print("Invalid phone number")

                else:
                    print("Contact does not exist")

            else:
                print("Invalid name...")




    @staticmethod
    def delete_contact():

        while True:
            name = input("Enter your name: ")
            if name.replace(" " , "").isalnum():

                if name in contacts.keys():

                    while True:
                        phone = input("Enter your phone number: ")
                        if phone.isnumeric():
                            phone = int(phone)

                            len_phone = len(str(phone))
                            if len_phone == 10:

                                if phone in contacts.values():

                                    del contacts[name]
                                    save_contacts()

                                    print(f"{name} : {phone} had deleted")
                                    print(contacts)

                                else:
                                    print("Contact does not exist")

                            else:
                                print("Invalid phone number")

                        else:
                            print("Invalid phone number")

                else:
                    print("Contact does not exist")

            else:
                print("Invalid name...")


    @staticmethod
    def show_contacts():
        print("--------------- CONTACT MENU ---------------")
        for key, value in contacts.items():
            print(f"{key} : {value}")


if os.path.exists(CSV_file):
    load_contacts()
else:
    save_contacts()



while True:
    print("1. Add contact")
    print("2. Search contact")
    print("3. Edit contact")
    print("4. Delete contact")
    print("5. Show contacts")
    print("6. Exit")

    choice = input("Please choose your choice: ")

    match choice:
        case "1":
            Contact.add_contact()
        case "2":
            Contact.search_contact()
        case "3":
            Contact.edit_contact()
        case "4":
            Contact.delete_contact()
        case "5":
            Contact.show_contacts()
        case "6":
            print("Goodbye!")
            break
        case _:
            print("Invalid choice Try again")



