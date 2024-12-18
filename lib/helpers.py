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
    employee=Employee.get_all()
    for employee in Employee:
     print(employee)
    


def find_employee_by_name():
    name = input("enter the employee's name:")
    employee = Employee.find_by_name(name)
    print(employee) if employee else print(f"Employee {name} Not Found")
    return employee

def find_employee_by_id():
    
    id = input("enter employee's id:")
    employee = Employee.find_by_id(id) if employee else print(f"empoyee {id} Not found")
    return employee


def create_employee():
    
    name = input("enter nemployee's name:")
    job_title = input("enter employee jobs title:") 
    Department_id = input("enter employee's department id:")
    employee = Employee.create(name,job_title,Department_id)
    print(f"success {employee}")
    return employee


def update_employee():
    
    id = input("enter employees id:")
    employee = Employee.find_by_id(id)
    if employee:
        name = input("enter employees new name:")
        employee.name = name
        job_title = input("enter employees new job title:") 
        employee.job.title = job_title
        Department_id = input("enter employees new department id:")
        employee.department_id = Department_id
        employee.update()
        print(f"success: {employee}")
        return employee
    else:
        print(f"employee {id} not found")
        return
def delete_employee():
    
    id = input("enter employees id:")
    employee = Employee.find_by_id(id)
    if employee:
        employee.delete()
        print(f"employee {id} deleted")
        return employee
    else:
        print(f"employee {id} not found")
        return


    
def list_department_employees():

    id = input("enter department id:")
    Department = Department.find_by_id(id)
    if Department:
        employee = Employee.find_by_id(id)
        print(employee)
        return employee
    else:
        print(f"department {id} not found")
        return