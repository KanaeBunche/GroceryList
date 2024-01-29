grocery_list = []



    # Make a fucntion to add a new item


    #Maka a fucntion to remove a new item

def view_list():
    if grocery_list:
        print("Your Grocery List:")
        for item in grocery_list:
            print(f"- {item}")
    else:
        print("Your grocery list is empty.")

    #Make a fucntion to clear the list

# Main program loop 
while True:
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Clear List")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        item = input("Enter the item to add: ")
        add_item(item)
    elif choice == '2':
        item = input("Enter the item to remove: ")
        remove_item(item)
    elif choice == '3':
        view_list()
    elif choice == '4':
        clear_list()
    elif choice == '5':
        print("Exiting...")
        
    else:
        print("Invalid choice. Please try again.")
