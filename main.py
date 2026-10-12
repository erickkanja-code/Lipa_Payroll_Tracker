class Employee:
    """
    Represents a single employee in the organisation.
    
    Attributes:
    
        name (str): The employees full name.
        job_title (str): The employees job title
        category (int): The employee category
        bank_name (str): The employee's bank name
        account_number (str): The employee's account number
        salary (int): The 
        id (int):
        
    """
    
    # You need to first use getters for the private variables, then use property so they can be accessed as properties, then modularise
    def __init__(self, name, job_title, category, 
                 bank_name, account_number, salary, id):
        self._name = name
        self._job_title = job_title
        self._category = category
        self._bank_name = bank_name
        self._account_number = account_number
        self._salary = salary
        # new_employee_record = {"id": id, "name": self.name, 
        #                        "job_title": self.job_title, 
        #                        "category": self.category, 
        #                        "bank_name": self.bank_name, 
        #                        "account_number": self.account_number, 
        #                        "salary": salary}
        # employee_records.append(new_employee_record)

    def calculate_salary(self, bonus):
        """Calculate the employee's gross salary.

        Args:
            bonus (int): The bonus added to the base salary.

        Returns:
            int: The employee's gross salary before deductions.
        """
        self.gross_salary = self._salary + bonus
        return self.gross_salary
    
    def apply_taxes(self):
        """Calculate the employee's salary after tax deductions.

        Returns:
            float: The salary remaining after a 30% tax deduction.
        """
        return self.gross_salary - (0.3 * self.gross_salary)
    
class FullTImeEmployee(Employee):
    """Represent a full-time employee.

    Inherits employee details and salary calculation methods from Employee.
    """
    
    pass


class ContractEmployee(Employee):
    """Represent an employee hired on a contract basis.

    Provides a salary calculation method that uses the base salary
    without adding a bonus.
    """
    def calculate_salary(self):
        """Calculate the employee's gross salary.

        Returns:
            int: The employee's base salary before deductions.
        """
        self.gross_salary = self._salary
        return self.gross_salary

class Intern(Employee):
    """Represent an intern in the organisation.

    Provides salary calculation without a bonus and returns the base
    salary without applying tax deductions.
    """   
    def calculate_salary(self):
        """Calculate the intern's gross salary.

        Returns:
            int: The intern's base salary before deductions.
        """
        self.gross_salary = self._salary
        return self.gross_salary
    def apply_taxes(self):
        """Return the intern's salary without tax deductions.

        Returns:
            int: The intern's base salary.
        """
        return self._salary
    







def add_new_employee():
    """Collect employee details and register a new employee.

    Prompts the user for employee information, creates an instance
    of the appropriate employee subclass, and stores it in the
    payroll data dictionary.
    """
    name = input("Enter the full employee name:")
    job_title = input("What's the employee's job title")
    category = input("Select the employee's category(1, 2 or 3):\n1. Full time employee \n2. Contract employee \n3. Intern ")
    bank_name = input("Enter bank name:")
    account_number = input("Enter bank account number:")
    salary = int(input("What is the employee's salary in Rwf:"))
    id = len(employee_payroll_data)
    
    if category == "1":
        new_employee = FullTImeEmployee(name, job_title, category, bank_name, account_number, salary, id)
        
    elif category == "2":
        new_employee = ContractEmployee(name, job_title, category, bank_name, account_number, salary, id)
    else:
        new_employee = Intern(name, job_title, category, bank_name, account_number, salary, id)
    employee_payroll_data[id] = new_employee

def generate_payslip():
    """Generate a payslip for a selected employee.

    Prompts the user for an employee ID, calculates the employee's
    gross and net salary, and prints the payslip.
    """
    employee_id = int(input("Kindly enter the id of the employee"))
    
    if employee_id in employee_payroll_data:
        if isinstance(employee_payroll_data[employee_id], FullTImeEmployee):
            gross_salary = employee_payroll_data[employee_id].calculate_salary(500)
        else:
            gross_salary = employee_payroll_data[employee_id].calculate_salary()
        net_salary = employee_payroll_data[employee_id].apply_taxes()
    
    print("|===============================|\n"
         f"|           PAYSLIP             |\n"
         f"|Name:{employee_payroll_data[employee_id]._name} |\n"
         f"|Job Title: {employee_payroll_data[employee_id]._job_title} |\n"
         f"|Job Title: {employee_payroll_data[employee_id]._category} |\n"
          "| Gross Salary   |  Net Salary  |\n"
         f"| {gross_salary} | {net_salary} |"
          )
    
def generate_all_payslips():
    """Calculate and print payslips for all registered employees.

    Iterates through the payroll data dictionary, calculates each
    employee's gross and net salary, and prints their payslip.
    """
    for employee in employee_payroll_data:
        if isinstance(employee_payroll_data[employee], FullTImeEmployee):
            gross_salary = employee_payroll_data[employee].calculate_salary(500)
        else:
            gross_salary = employee_payroll_data[employee].calculate_salary()
        net_salary = employee_payroll_data[employee].apply_taxes()  
        print("|===============================|\n"
            f"|           PAYSLIP             |\n"
            f"|Name:{employee_payroll_data[employee]._name} |\n"
            f"|Job Title: {employee_payroll_data[employee]._job_title} |\n"
            f"|Job Title: {employee_payroll_data[employee]._category} |\n"
            "| Gross Salary   |  Net Salary  |\n"
            f"| {gross_salary} | {net_salary} |\n\n"
            )
    


# employee_records = []
employee_payroll_data = {}
while True:
    add_new_employee()
    generate_all_payslips()





