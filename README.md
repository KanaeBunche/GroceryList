

## Python Local Host Setup Guide

This guide will walk you through the steps to set up a local host environment for Python development on your machine.

### Prerequisites

Before you begin, ensure that you have the following installed on your system:

- Python (version 3.x recommended)
- pip (Python package manager)

### Steps to Set Up Local Host

1. **Clone Repository**: Clone the repository to your local machine using the following command:
   ```
   git clone <repository_url>
   ```

2. **Navigate to Project Directory**: Change your current directory to the project folder:
   ```
   cd <project_directory>
   ```

3. **Create Virtual Environment (Optional)**: It's a good practice to create a virtual environment for your Python projects to isolate dependencies. To create a virtual environment, run:
   ```
   python -m venv <venv_name>
   ```

4. **Activate Virtual Environment (Optional)**: Activate the virtual environment. The command varies based on your operating system:
   - On Windows:
     ```
     <venv_name>\Scripts\activate
     ```
   - On macOS and Linux:
     ```
     source <venv_name>/bin/activate
     ```

5. **Install Dependencies**: Install the project dependencies using pip:
   ```
   pip install -r requirements.txt
   ```

6. **Run the Application**: Run the Python application using the following command:
   ```
   python app.py
   ```

7. **Access Local Host**: Open your web browser and navigate to `http://localhost:5000` to view the application running locally.

8. **Interact with the Application**: You can now interact with the application and explore its features.

### Additional Notes

- Make sure to replace `<repository_url>` and `<project_directory>` with the actual URL of the repository and the name of your project directory, respectively.
- `<venv_name>` represents the name you choose for your virtual environment.
- If you encounter any issues during the setup process, refer to the project documentation or seek help from the project maintainers.

Happy coding!

# Grocery List Manager

This is a simple Python program that allows users to manage their grocery lists. Users can add items to the list, remove items, view the current list, and clear the entire list when needed.

## Functions:

### 1. add_item(item)
- Adds the specified item to the grocery list.
- Parameters:
  - `item`: The item to be added to the grocery list.


### 2. remove_item(item)
- Removes the specified item from the grocery list if it exists.
- Parameters:
  - `item`: The item to be removed from the grocery list.


### 3. view_list()
- Displays the current contents of the grocery list.


### 4. clear_list()
- Clears all items from the grocery list.


## Usage:

1. Run the Python script.
2. Choose from the following options:
   - `1. Add Item`: Add an item to the grocery list.
   - `2. Remove Item`: Remove an item from the grocery list.
   - `3. View List`: View the current items in the grocery list.
   - `4. Clear List`: Clear all items from the grocery list.
   - `5. Exit`: Exit the program.





This program provides a simple interface for managing grocery lists using Python. Users can easily add, remove, view, and clear items from their list.
