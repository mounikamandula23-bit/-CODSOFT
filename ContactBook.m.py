import os
contacts=[]
def clear_screen():
    os.system('cls' if os.name=='nt' else 'clear')
def add_contact():
    clear_screen()
    print("Add New Contact:")
    name=input("Name:")
    phone=input("Phone Number:")
    email=input("Email:")
    address=input("Address:")
    contact={
        "name":name.strip(),
        "phone":phone.strip(),
        "email":email.strip(),
        "address":address.strip()
        }
    contacts.append(contact)
    print("\nContact added successfully!")
def search_contacts():
    clear_screen()
    if not contacts:
        print("No contacts found.")
        return
    print("Contact List:\n")
    for i,contact in enumerates(contacts,start=1):
        print(f"{i}.{contact['name']}-{contact['phone']}")
def search_contact():
    clear_screen()
    query=input("Enter name or phone to search:").lower()
    found=False
    for contact in contacts:
        if query in contact['name'].lower() or query in contact['phone']:
            print(f"Name:{contact['name']}")
            print(f"Phone:{contact['phone']}")
            print(f"Email:{contact['email']}")
            print(f"Address:{contact['address']}")
            found=True
            break
        if not found:
            print("No matching contact found.")
def update_contact():
    clear_screen()
    name=input("Enter the name of the contact to update:").lower()
    for contact in contacts:
        if name==contact['name'].lower():
            print("\nLeave blank to keep current value.")
            contact['name']=input(f"New Name({contact['name']}):") or contact['name']
            contact['phone']=input(f"New Phone({contact['phone']}):") or contact['phone']
            contact['email']=input(f"New Email({contact['email']}):") or contact['email']
            contact['address']=input(f"New Address({contact['address']}):") or contact['address']
            print("\nContact updated successfully!")
    print("Contact not found.")
def delete_contact():
    clear_screen()
    name=input("Enter the name of the contact to delete:").lower()
    for i,contacts in enumerate(contacts):
        if name==contact['name'].lower():
            del contacts[i]
            print("\nContact deleted successfully!")
    print("Contact not found.")
def main():
    while True:
        print("\n---Contact Book---")
        print("1.Add Contact")
        print("2.View Contact List")
        print("3.Search Contact")
        print("4.Update Contact")
        print("5.Delete contact")
        print("6.Exit")
        choice=input("\nEnter your choice(1-6):")
        if choice=='1':
            add_contact()
        elif choice=='2':
            view_contacts()
        elif choice=='3':
            search_contact()
        elif choice=='4':
            update_contact()
        elif choice=='5':
            delete_contact()
        elif choice=='6':
            print("Existing Contact Book.Goodbye!")
            break
        else:
            print("Invalid choice.Please enter a number between 1 and 6.")
        input("\nPress Enter to continue...")
        clear_screen()
if __name__=="__main__":
    main()
                                  
              
    
