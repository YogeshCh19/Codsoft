#ContactBook which can Add,View,Search,Update and Delete a contact

contact={}
   
def Contact_Add():
    name = input("Enter Contact Name: ")
    phone = input("Enter Mobile Number: ")
    contact[name] = phone

def searching():
    search_contact = input("Enter the contact name to be searched: ")
    if search_contact in contact:
        print("contact found")
        print(search_contact, ":", contact[search_contact])
    else:
        print("contact not found")


def View_contact():
    if not contact:
            print("empty contact book")
    else:
        print("name\t\tContact Number")
        for key in contact:
            print("{}\t\t{}".format(key,contact.get(key)))

def Contact_Edit():
    edit_contact = input("Enter contact to be edited: ")
    if edit_contact in contact:
        phone = input("enter mobile number: ")
        contact[edit_contact] = phone
        print("contact updated")
    else:
        print("Contact is not found")

def Contact_Delete():
    del_contact = input('Enter the contact to be deleted: ')
    if del_contact in contact:
        confirm = input("Do you want to delete the contact y/n?: ")
        confirm = confirm.lower()
        if confirm =='y':
            contact.pop(del_contact)
            print("Contact Deleted")
    else:
        print("Contact is not found")
    
while True:
    choice = int(input("\n 1.Add Contact \n 2. View Contact \n 3. Search Contact \n 4. Update Contact \n 5. Delete Contact \n 6. Exit \n "))
    if choice == 1:
        Contact_Add()

    elif choice == 2:
        View_contact()

    elif choice == 3:
        searching()

    elif choice == 4:
        Contact_Edit()

    elif choice == 5:
        Contact_Delete()

    elif choice == 6:
        print("Contact Book Closed")
        exit()
    else:
        break