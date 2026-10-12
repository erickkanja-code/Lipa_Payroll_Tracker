from employee import FullTImeEmployee
from utils import employee_payroll_data, get_int


def generate_payslip():
    """Generate a payslip for a selected employee.

    Prompts the user for an employee ID, calculates the employee's
    gross and net salary, and prints the payslip.
    """
    employee_id = get_int("Kindly enter the id of the employee", min_value=0)
    
    if employee_id not in employee_payroll_data:
        print(f"No employee found with id {employee_id}.")
        return

    if isinstance(employee_payroll_data[employee_id], FullTImeEmployee) or isinstance(employee_payroll_data[employee_id], ContractEmployee):
        bonus = get_int(f"Enter the bonus amount for employee id: {employee_id} name: {employee_payroll_data[employee_id].name}", min_value=0)
        gross_salary = employee_payroll_data[employee_id].calculate_salary(bonus)
    else:
        gross_salary = employee_payroll_data[employee_id].calculate_salary()
    net_salary = employee_payroll_data[employee_id].apply_taxes()
    

    print(
        f"""
        =================================
                    PAYSLIP
        =================================
        Name:       {employee_payroll_data[employee_id].name}
        Job Title:  {employee_payroll_data[employee_id].job_title}
        Category:   {employee_payroll_data[employee_id].category}
        ---------------------------------
        Gross Salary:  {gross_salary:,.2f} RWF
        Net Salary:    {net_salary:,.2f} RWF
        =================================
        """
    )

    
def generate_all_payslips():
    """Calculate and print payslips for all registered employees.

    Iterates through the payroll data dictionary, calculates each
    employee's gross and net salary, and prints their payslip.
    """
    if not employee_payroll_data:
        print("No employees have been added yet.")
        return
    for employee in employee_payroll_data:
        if isinstance(employee_payroll_data[employee], FullTImeEmployee) or isinstance(employee_payroll_data[employee], ContractEmployee):
            bonus = get_int(f"Enter bonus amount for employee id: {employee} name: {employee_payroll_data[employee].name}:", min_value=0)
            gross_salary = employee_payroll_data[employee].calculate_salary(bonus)
        else:
            gross_salary = employee_payroll_data[employee].calculate_salary()
        net_salary = employee_payroll_data[employee].apply_taxes()  

        print(
            f"""
            =================================
                        PAYSLIP
            =================================
            Name:       {employee_payroll_data[employee].name}
            Job Title:  {employee_payroll_data[employee].job_title}
            Category:   {employee_payroll_data[employee].category}
            ---------------------------------
            Gross Salary:  {gross_salary:,.2f} RWF
            Net Salary:    {net_salary:,.2f} RWF
            =================================
            """
        )
