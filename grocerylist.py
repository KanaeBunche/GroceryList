grocery_list = []

def add_item(item):
    grocery_list.append(item)
    print(f"{item} has been added to your grocery list.")

def remove_item(item):
    if item in grocery_list:
        grocery_list.remove(item)
        print(f"{item} has been removed from your grocery list.")
    else:
        print(f"{item} is not in your grocery list.")

def view_list():
    if grocery_list:
        print("Your Grocery List:")
        for item in grocery_list:
            print(f"- {item}")
    else:
        print("Your grocery list is empty.")

def clear_list():
    grocery_list.clear()
    print("Your grocery list has been cleared.")

# Main program loop
while True:
    print("\n1. Add Item")
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
        break
    else:
        print("Invalid choice. Please try again.")
