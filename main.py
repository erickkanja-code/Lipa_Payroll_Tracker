class Employee:
    def __init__(self, name, job_title, category, 
                 bank_name, account_number, salary, id):
        self.name = name
        self.job_title = job_title
        self.category = category
        self.bank_name = bank_name
        self.account_number = account_number
        self.salary = salary
        new_employee_record = {"id": id, "name": self.name, 
                               "job_title": self.job_title, 
                               "category": self.category, 
                               "bank_name": self.bank_name, 
                               "account_number": self.account_number, 
                               "salary": salary}
        employee_records.append(new_employee_record)

    def calculate_salary(self, bonus):
        self.gross_salary = self.salary + bonus
        return self.gross_salary
    
    def apply_taxes(self):
        return self.gross_salary - (0.3 * self.gross_salary)
    
class FullTImeEmployee(Employee):
    pass


class ContractEmployee(Employee):
    def calculate_salary(self):
        self.gross_salary = self.salary
        return self.gross_salary

class Intern(Employee):
        
    def calculate_salary(self):
        self.gross_salary = self.salary
        return self.gross_salary
    def apply_taxes(self):
        return self.salary
    







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
        
    elif category == "2":
        new_employee = ContractEmployee(name, job_title, category, bank_name, account_number, salary, id)
    else:
        new_employee = Intern(name, job_title, category, bank_name, account_number, salary, id)
    employee_payroll_data[id] = new_employee

def generate_payslip():
    employee_id = int(input("Kindly enter the id of the employee"))
    
    if employee_id in employee_payroll_data:
        if isinstance(employee_payroll_data[employee_id], FullTImeEmployee):
            gross_salary = employee_payroll_data[employee_id].calculate_salary(500)
        else:
            gross_salary = employee_payroll_data[employee_id].calculate_salary()
        net_salary = employee_payroll_data[employee_id].apply_taxes()
    
    print("|===============================|\n"
         f"|           PAYSLIP             |\n"
         f"|Name:{employee_payroll_data[employee_id].name} |\n"
         f"|Job Title: {employee_payroll_data[employee_id].job_title} |\n"
         f"|Job Title: {employee_payroll_data[employee_id].category} |\n"
          "| Gross Salary   |  Net Salary  |\n"
         f"| {gross_salary} | {net_salary} |"
          )
    
def generate_all_payslips():
    for employee in employee_payroll_data:
        if isinstance(employee_payroll_data[employee], FullTImeEmployee):
            gross_salary = employee_payroll_data[employee].calculate_salary(500)
        else:
            gross_salary = employee_payroll_data[employee].calculate_salary()
        net_salary = employee_payroll_data[employee].apply_taxes()  
        print("|===============================|\n"
            f"|           PAYSLIP             |\n"
            f"|Name:{employee_payroll_data[employee].name} |\n"
            f"|Job Title: {employee_payroll_data[employee].job_title} |\n"
            f"|Job Title: {employee_payroll_data[employee].category} |\n"
            "| Gross Salary   |  Net Salary  |\n"
            f"| {gross_salary} | {net_salary} |\n\n"
            )
    
"""
Get user input of the employee ID and bonus -> Search the employee records using ID -> Run that objects method for calculating the salary -> Run the apply taxes method -> Update the payroll data dictionary -> Generate payslip from 
For apply taxes: full time will get 30% applied 
"""


employee_records = []
employee_payroll_data = {}
while True:
    add_new_employee()
    generate_all_payslips()





