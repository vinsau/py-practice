import os
import sys
import time

contacts = {}   

def add_contact():
    def name_validation(value) -> bool:
        value = value.strip()
        if value.isnumeric() or value == "":
            print("Name must not be pure numeric and empty. Please try again...")
            return False
        else:
            return True

    while True:
        display_header("ADD NEW CONTACT")
        name = input("\nEnter name: ")
        if not name_validation(name):
            press_enter()
            continue
        else:
            email = input(("Enter email: "))
            address = input(("Enter address: "))

            contacts[name] = {"email": email, "address": address}
            print("\nContact added sucessfully!")
            break
    press_enter()

def search_contact():
    while True:
        display_header("SEARCH CONTACT")
        
        if not isContactsEmpty():
            count = 0
            for k in contacts.keys():
                count += 1
            
            print(f"\nSearch through {count} contact/s:")
            search = input("Enter any details: ")
            if search == "":
                print("Search cannot be empty...")
                press_enter()
                continue
            for name, info in contacts.items():
                if search == name or search == info:
                    print("Contact Found!\n")
                    print(f"{name} - {info['email']}, - {info['address']}\n")
                    break
                else:
                    print("\nContact not found...")
                    if not tryagain():
                        break
        else:
            break         
    press_enter()

def delete_contact():
    while True:
        display_header("DELETE CONTACT")

        if not isContactsEmpty():
            name = input("\nEnter the name you want to delete or Q to go back: ")
            response = name.lower()
            if response != 'q':
                if name in contacts:
                    contacts.pop(name)
                    print("\nContact deleted sucessfully!")
                    break
                else:
                    print("Contact not found...")
                    if not tryagain():
                        break
            else:
                break
        else:
            break
        
    press_enter()

def update_contact():
    def verify_input(response) -> bool:
        if response == "":
            return False
        else:
            return True
    while True:
        display_header("UPDATE CONTACT")

        if not isContactsEmpty():
            print("\nName change is not allowed, you need to create a new one instead...")
            name = input("Enter the name you want to update: ")
            if name in contacts:
                print("\nContact Found!\n")
                temp_email = input(f"Email [{contacts[name]["email"]}]: ")
                
                if (verify_input(temp_email)):
                    contacts[name]["email"] = temp_email
                
                temp_address = input(f"Address [{contacts[name]["address"]}]: ")
                if (verify_input(temp_email)):
                    contacts[name]["address"] = temp_address
                print("\nContact updated successfully!")
                break
            else:
                print("Contact not found...")
                if not tryagain():
                   break
        else:
            break
    press_enter()

def display_contacts():
    display_header("DISPLAY CONTACTS")
    isContactsEmpty()
    press_enter()

def display_header(message):
    os.system("clear")
    print(message)

def isContactsEmpty() -> bool:
    def display_data():
        def line(length = 70):
            print("-" * length)
            
        print("\nCurrent contacts:\n")
        line()
        print(f"| {"NAME":^24} | {"EMAIL":^21} | {"ADDRESS":^15} |")
        line()
        for name, info in contacts.items():
            print(f"| {name:^24} | {info['email']:^21} | {info['address']:^15} |")
        line()

    if not contacts:
        print("\nThere are currently no contacts\n")
        return True
    else:
        display_data()
        return False

def tryagain() -> bool:
    choice = input("\nDo you want to continue?(Y/N): ")
    if choice.lower() == 'y':
        return True
    else:
        run()
    
def press_enter():
    input("\nPress Enter to continue...")

def run():
    def display_menu():
        display_header("SIMPLE CONTACT BOOK\n")
        print("[1] Add Contact")
        print("[2] Search Contact")
        print("[3] Delete Contact")
        print("[4] Update Contact")
        print("[5] Display Contact")
        print("[6] Exit")

    def countdown():
        for i in range(3, 0, -1):
            print(i)
            time.sleep(0.5)
        
    while True:
        display_menu()
        try:
            choice = int(input("\nEnter your choice (1-6): "))
        except ValueError:
            print("Invalid input. Please try again...")
            press_enter()
            continue

        match choice:
            case 1:
                add_contact()
            case 2:
                search_contact()
            case 3:
                delete_contact()
            case 4:
                update_contact()
            case 5:
                display_contacts()
            case 6:
                print("THANK YOU USING SIMPLE CONTACT BOOK!")
                print("Exiting the program...")
                countdown()
                sys.exit(0)
            case _:
                input("Invalid choice! Only choose from 1-6. Press Enter to continue...")

run()