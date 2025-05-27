from models.department import Department
from models.employee import Employee


def exit_program():
    print("Goodbye!")
    exit()

# We'll implement the department functions in this lesson


def list_departments():
    departments = Department.get_all()
    for department in departments:
        print(department)


def find_department_by_name():
    name = input("Enter the department's name: ")
    department = Department.find_by_name(name)
    print(department) if department else print(
        f'Department {name} not found')


def find_department_by_id():
    # use a trailing underscore not to override the built-in id function
    id_ = input("Enter the department's id: ")
    department = Department.find_by_id(id_)
    print(department) if department else print(f'Department {id_} not found')


def create_department():
    name = input("Enter the department's name: ")
    location = input("Enter the department's location: ")
    try:
        department = Department.create(name, location)
        print(f'Success: {department}')
    except Exception as exc:
        print("Error creating department: ", exc)


def update_department():
    id_ = input("Enter the department's id: ")
    if department := Department.find_by_id(id_):
        try:
            name = input("Enter the department's new name: ")
            department.name = name
            location = input("Enter the department's new location: ")
            department.location = location

            department.update()
            print(f'Success: {department}')
        except Exception as exc:
            print("Error updating department: ", exc)
    else:
        print(f'Department {id_} not found')


def delete_department():
    id_ = input("Enter the department's id: ")
    if department := Department.find_by_id(id_):
        department.delete()
        print(f'Department {id_} deleted')
    else:
        print(f'Department {id_} not found')


# You'll implement the employee functions in the lab

def list_employees():
    #pass
    employees = Employee.get_all()
    if not employees:
        print("No employees found.")
    else:
        for emp in employees:
            print(emp)


def find_employee_by_name():
    #pass
    name = input("Enter the employee's name: ")
    employee = Employee.find_by_name(name)
    if employee:
        print(employee)
    else:
        print(f'Employee {name} not found')   


def find_employee_by_id():
    #pass
    id_ = input("Enter the employee's id: ")
    employee = Employee.find_by_id(id_)
    if employee:
        print(employee)
    else:
        print(f'Employee {id_} not found')


def create_employee():
    #pass
    name = input("Enter the employee's name: ")
    job_title = input("Enter the employee's job title: ")
    department_id = input("Enter the employee's department id: ")
    
    try:
        department_id = int(department_id)
        employee = Employee.create(name, job_title, department_id)
        print(f'Success: {employee}')
    except Exception as e:
        print("Error creating employee:", e)


def update_employee():
    #pass
    id_ = input("Enter the employee's id to update: ")
    employee = Employee.find_by_id(id_)
    
    if employee:
        try:
            name = input(f"Enter new name (current: {employee.name}): ")
            job_title = input(f"Enter new job title (current: {employee.job_title}): ")
            department_id = input(f"Enter new department ID (current: {employee.department_id}): ")
             
            employee.name = name
            employee.job_title = job_title
            employee.department_id = int(department_id)
            
            employee.update()
            print(f'Success: {employee}')
        except Exception as e:
            print("Error updating employee:", e)     

def delete_employee():
    #pass
    id_ = input("Enter the employee's id to delete: ")
    employee = Employee.find_by_id(id_)
    if employee:
        employee.delete()
        print(f'Employee {id_} deleted')
    else:
        print(f'Employee {id_} not found')


def list_department_employees():
   # pass
    department_id = input("Enter the department's id to list employees: ")
    try:
        department_id = int(department_id)
        employees = Employee.find_by_department_id(department_id)
        if employees:
            for emp in employees:
                print(emp)
        else:
            print(f'No employees found in department {department_id}')
    except ValueError:
        print("Invalid department ID. Please enter a valid integer.")