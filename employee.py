from utils import get_text, get_int, get_category, get_account_number, employee_payroll_data

class Employee:
    """
    Represents a single employee in the organisation.
    
    Attributes:
    
        name (str): The employees full name.
        job_title (str): The employees job title
        category (int): The employee category
        bank_name (str): The employee's bank name
        account_number (str): The employee's account number
        id (int): The employee's unique id
        
    """
    
    # then modularise
    def __init__(self, name, job_title, category, 
                 bank_name, account_number, id):
        self.name = name
        self.job_title = job_title
        self.category = category
        self.bank_name = bank_name
        self.account_number = account_number
        # self._salary = salary

    
    def calculate_salary(self, bonus):
        """Calculate the employee's gross salary.

        Args:
            bonus (int): The bonus added to the base salary.

        Returns:
            int: The employee's gross salary before deductions.
        """
        self.gross_salary = self.get_salary + bonus
        return self.gross_salary
    
    def apply_taxes(self):
        """Calculate the employee's salary after tax deductions.

        Returns:
            float: The salary remaining after a 30% tax deduction.
        """
        return self.gross_salary - (self.get_tax * self.gross_salary)
    
class FullTImeEmployee(Employee):
    """Represent a full-time employee.

    Inherits employee details and salary calculation methods from Employee.
    """
    @property
    def get_salary(self):
        """Getter for full time employee's salary"""
        self.__salary = 900_000
        return self.__salary
    
    @property  
    def get_tax(self):
        """Getter for full time employee tax amount"""
        self.__tax = 0.35
        return self.__tax
    
class ContractEmployee(Employee):
    """Represent an employee hired on a contract basis.

    Provides a salary calculation method that uses the base salary
    without adding a bonus.
    """
    @property
    def get_salary(self):
        """Getter for full time employee's salary"""
        self.__salary = 500_000
        return self.__salary
    
    @property  
    def get_tax(self):
        """Getter for full time employee tax amount"""
        self.__tax = 0.25
        return self.__tax
    
    def calculate_salary(self, bonus):
        """Calculate the employee's gross salary.

        Args:
            bonus (int): The bonus added to the base salary.

        Returns:
            int: The employee's gross salary before deductions.
        """
        self.gross_salary = self.get_salary + bonus
        return self.gross_salary
    

class Intern(Employee):
    """Represent an intern in the organisation.

    Provides salary calculation without a bonus and returns the base
    salary without applying tax deductions.
    """   
    @property
    def get_salary(self):
        """Getter for full time employee's salary"""
        self.__salary = 200_000
        return self.__salary
    
    @property  
    def get_tax(self):
        """Getter for full time employee tax amount"""
        self.__tax = 1
        return self.__tax
    
    def calculate_salary(self):
        """Calculate the employee's gross salary.

        Args:
            bonus (int): The bonus added to the base salary.

        Returns:
            int: The employee's gross salary before deductions.
        """
        self.gross_salary = self.get_salary
        return self.gross_salary
    

def add_new_employee():
    """Collect employee details and register a new employee.

    Prompts the user for employee information, creates an instance
    of the appropriate employee subclass, and stores it in the
    payroll data dictionary.
    """
    name = get_text("Enter the full employee name:")
    job_title = get_text("What's the employee's job title")
    category = get_category("Select the employee's category(1, 2 or 3):\n1. Full time employee \n2. Contract employee \n3. Intern ")
    bank_name = get_text("Enter bank name:")
    account_number = get_account_number("Enter bank account number:")
    # salary = int(input("What is the employee's salary in Rwf:"))
    id = len(employee_payroll_data)
    
    if category == "1":
        new_employee = FullTImeEmployee(name, job_title, category, bank_name, account_number, id)
    elif category == "2":
        new_employee = ContractEmployee(name, job_title, category, bank_name, account_number, id)
    else:
        new_employee = Intern(name, job_title, category, bank_name, account_number, id)
    employee_payroll_data[id] = new_employee
    print(f"{new_employee.name} added succesfully")
    
def view_single_employee():
    employee_id = get_int("Enter the employee id:", min_value=0)
    if employee_id not in employee_payroll_data:
        print(f"No employee found with id {employee_id}.")
        return
    for id in employee_payroll_data:
        if id == employee_id:
            employee = employee_payroll_data[id]
            print(
                f"""
                =================================
                    EMPLOYEE DETAILS
                =================================
                Employee ID:      {id}
                Employee Name:    {employee.name}
                Job Category:     {employee.category}
                Bank Name:        {employee.bank_name}
                Bank Account No.: {employee.account_number}
                =================================
                """
            )
            
def view_all_employees():
    if not employee_payroll_data:
        print("No employees have been added yet.")
        return
    for id in employee_payroll_data:
        employee = employee_payroll_data[id]
        print(
            f"""
            =================================
                EMPLOYEE DETAILS
            =================================
            Employee ID:      {id}
            Employee Name:    {employee.name}
            Job Category:     {employee.category}
            Bank Name:        {employee.bank_name}
            Bank Account No.: {employee.account_number}
            =================================
            """
        )
        