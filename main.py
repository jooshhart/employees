import time
from employee_directory import *

def insert_data():
    while True:
        print("\nInsert Data Menu:")
        print("1) Insert Department")
        print("2) Insert Employee")
        print("3) End Insert")
        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Enter department name: ")
            insert_department(name)
            print(f"Department '{name}' added.")
            time.sleep(5)
        elif choice == '2':
            name = input("Enter employee name: ")
            email = input("Enter employee email: ")
            department_name = input("Enter department name: ")
            insert_employee(name, email, department_name)
            print(f"Employee '{name}' added.")
            time.sleep(5)
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")
            time.sleep(5)

def find_data():
    while True:
        print("\nFind Data Menu:")
        print("1) Find Departments")
        print("2) Find Employees")
        print("3) Find Employee")
        print("4) End Find")
        choice = input("Choose an option: ")

        if choice == '1':
            departments = get_departments()
            print("\nDepartments:")
            for dept in departments:
                print(dept)
            time.sleep(5)
        elif choice == '2':
            employees = get_employees()
            print("\nEmployees:")
            for emp in employees:
                print(emp[1])  # Display only the employee name
            time.sleep(5)
        elif choice == '3':
            name = input("Enter employee name to search: ")
            employees = search_employee_by_name(name)
            print("\nSearch Results:")
            for emp in employees:
                print(emp)
            time.sleep(5)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")
            time.sleep(5)

def change_data():
    while True:
        print("\nChange Data Menu:")
        print("1) Load Department")
        print("2) Load Employee")
        print("3) End Change")
        choice = input("Choose an option: ")

        if choice == '1':
            departments = get_departments()
            print("\nDepartments:")
            for dept in departments:
                print(dept)
            old_name = input("Enter department name to change: ")
            new_name = input("Enter new department name: ")
            update_department(old_name, new_name)
            print(f"Department name changed from '{old_name}' to '{new_name}'.")
            time.sleep(5)
        elif choice == '2':
            employees = get_employees()
            print("\nEmployees:")
            for emp in employees:
                print(emp)
            employee_id = int(input("Enter employee ID to change: "))
            while True:
                print("\nEmployee Change Menu:")
                print("1) Name")
                print("2) Email")
                print("3) Department")
                print("4) End Employee Change")
                sub_choice = input("Choose an option: ")

                if sub_choice == '1':
                    new_name = input("Enter new name: ")
                    update_employee(employee_id, name=new_name)
                    print(f"Employee name changed to '{new_name}'.")
                    time.sleep(5)
                elif sub_choice == '2':
                    new_email = input("Enter new email: ")
                    update_employee(employee_id, email=new_email)
                    print(f"Employee email changed to '{new_email}'.")
                    time.sleep(5)
                elif sub_choice == '3':
                    new_department = input("Enter new department: ")
                    update_employee(employee_id, department_name=new_department)
                    print(f"Employee department changed to '{new_department}'.")
                    time.sleep(5)
                elif sub_choice == '4':
                    break
                else:
                    print("Invalid choice. Please try again.")
                    time.sleep(5)
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")
            time.sleep(5)

def delete_data():
    while True:
        print("\nDelete Data Menu:")
        print("1) Delete Department")
        print("2) Delete Employee")
        print("3) End Delete")
        choice = input("Choose an option: ")

        if choice == '1':
            departments = get_departments()
            print("\nDepartments:")
            for dept in departments:
                print(dept)
            name = input("Enter department name to delete: ")
            confirm = input(f"Are you sure you want to delete department '{name}' and all its employees? (yes/no): ")
            if confirm.lower() == 'yes':
                delete_department(name)
                print(f"Department '{name}' and all its employees deleted.")
                time.sleep(5)
        elif choice == '2':
            employees = get_employees()
            print("\nEmployees:")
            for emp in employees:
                print(emp)
            name = input("Enter employee name to delete: ")
            confirm = input(f"Are you sure you want to delete employee '{name}'? (yes/no): ")
            if confirm.lower() == 'yes':
                delete_employee(name)
                print(f"Employee '{name}' deleted.")
                time.sleep(5)
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")
            time.sleep(5)

def main_menu():
    while True:
        print("\nMain Menu:")
        print("1) Insert Data")
        print("2) Find Data")
        print("3) Change Data")
        print("4) Delete Data")
        print("5) Quit")
        choice = input("Choose an option: ")

        if choice == '1':
            insert_data()
        elif choice == '2':
            find_data()
        elif choice == '3':
            change_data()
        elif choice == '4':
            delete_data()
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
            time.sleep(5)

if __name__ == "__main__":
    # Initialize the database
    create_tables()

    # Start the main menu
    main_menu()