class Employee:
    def __init__(self, name, job_title, category, 
                 bank_name, account_number, salary, id):
        self.name = name
        self.job_title = job_title
        self.category = category
        self.bank_name = bank_name
        self.account_number = account_number
        self.salary = salary
        new_employee_record = {"id": id, "name": self.name, "job_title": self.job_title, "category": self.category, "bank_name": self.bank_name, "account_number": self.account_number, "salary": salary}
        employee_records.append(new_employee_record)
    
    
    
    
        
class FullTImeEmployee(Employee):
    def apply_taxes(self):
        return self.salary - (0.3 * self.salary)


class ContractEmployee(Employee):
    pass

class Intern(Employee):
    pass
    







def add_new_employee():
    name = input("Enter the full employee name:")
    job_title = input("What's the employee's job title")
    category = input("Select the employee's category(1, 2 or 3):\n1. Full time employee \n2. Contract employee \n3. Intern ")
    bank_name = input("Enter bank name:")
    account_number = input("Enter bank account number:")
    salary = int(input("What is the employee's salary in Rwf:"))
    id = len(employee_records)
    
    if category == "1":
        new_employee = FullTImeEmployee(name, job_title, category, bank_name, account_number, salary, id)
        print(new_employee.apply_taxes())
    elif category == "2":
        new_employee = ContractEmployee(name, job_title, category, bank_name, account_number, salary, id)
    else:
        new_employee = Intern(name, job_title, category, bank_name, account_number, salary, id)


employee_records = []
while True:
    add_new_employee()



