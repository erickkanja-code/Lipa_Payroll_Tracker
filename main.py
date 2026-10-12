from employee import add_new_employee, view_all_employees, view_single_employee
from payroll import generate_payslip, generate_all_payslips
from utils import get_int

            

    


while True:

    menu_option = get_int(
            "\n=================================\n"
            "       LIPA PAYROLL TRACKER\n"
            "=================================\n"
            "Please select an option:\n\n"
            "1. Add employee\n"
            "2. View all employees\n"
            "3. View employee by ID\n"
            "4. Generate all payslips\n"
            "5. Generate payslip by ID\n"
            "6. Quit\n"
            "=================================\n"
            "Enter your choice (1-6): "
    )
    if menu_option == 1:
        add_new_employee()
    elif menu_option == 2:
        view_all_employees()
    elif menu_option == 3:
        view_single_employee()
    elif menu_option == 4:
        generate_all_payslips()
    elif menu_option == 5:
        generate_payslip()
    elif menu_option == 6:
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 6.")