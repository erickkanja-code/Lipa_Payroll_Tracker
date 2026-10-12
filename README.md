# Lipa Payroll Tracker

A command-line Python application for managing employee records and generating payslips for full-time employees, contract employees, and interns.

## Features

- Register employees with their personal and banking details.
- View all registered employees or search by employee ID.
- Calculate gross salaries based on employee category and bonuses.
- Apply category-specific tax rates to calculate net salaries.
- Generate individual payslips or payslips for all employees.
- Validate user input to handle invalid menu choices, employee IDs, categories, and bonus amounts.
## Requirements

- Python 3.10 or later
- [Poetry](https://python-poetry.org/) for dependency and virtual environment management

## Setup

1. Clone the repository:

   ```bash
   git clone <repository-url>
   ```

2. Navigate to the project directory:

   ```bash
   cd <project-directory>
   ```

3. Install project dependencies:

   ```bash
   poetry install
   ```

4. Run the application:

   ```bash
   poetry run python main.py
   ```

   Replace `main.py` with the name of your Python file if different.

Alternatively, activate Poetry's virtual environment:

```bash
poetry shell
```

Then run:

```bash
python main.py
```

## Dependency Management

Poetry manages the project's dependencies and virtual environment using `pyproject.toml` and `poetry.lock`.

To add a dependency:

```bash
poetry add <package-name>
```

To install dependencies from the existing project configuration:

```bash
poetry install
```

## Usage

When the application starts, a menu appears with the following options:

```text
=================================
       LIPA PAYROLL TRACKER
=================================
Please select an option:

1. Add employee
2. View all employees
3. View employee by ID
4. Generate all payslips
5. Generate payslip by ID
6. Quit
=================================
Enter your choice (1-6):
```

Enter the number corresponding to the action you want to perform.

### Adding an employee

Select option `1` and provide the employee's name, job title, employment category, bank name, and account number.

Available employee categories:

- **1:** Full-time employee
- **2:** Contract employee
- **3:** Intern

### Viewing employee records

- Select option `2` to display all registered employees.
- Select option `3` to display an employee's details using their ID.

### Generating payslips

- Select option `4` to generate payslips for all registered employees.
- Select option `5` to generate a payslip for one employee using their ID.

Full-time and contract employees are prompted for a bonus amount. Interns receive their base salary without an additional bonus.

### Exiting

Select option `6` to exit the application.

## Salary Calculation Rules

| Employee category | Base salary | Tax rate |
|---|---:|---:|
| Full-time employee | 900,000 RWF | 35% |
| Contract employee | 500,000 RWF | 25% |
| Intern | 200,000 RWF | 0% effectively |

Full-time and contract employees receive any bonus entered during payslip generation. Interns do not receive a bonus through the current calculation method.

Gross salary is calculated as:

```text
Gross Salary = Base Salary + Bonus
```

For full-time and contract employees:

```text
Net Salary = Gross Salary - (Tax Rate × Gross Salary)
```

For interns, the current implementation returns the base salary as net salary.

## Sample Output

Example payslip for a full-time employee with a base salary of 900,000 RWF and a bonus of 50,000 RWF:

```text
=================================
            PAYSLIP
=================================
Name:       Jane Doe
Job Title:  Software Engineer
Category:   1
---------------------------------
Gross Salary:  950,000.00 RWF
Net Salary:    617,500.00 RWF
=================================
```

The example uses a 35% tax rate, resulting in a net salary of 617,500 RWF.

## Technologies

- Python
- Object-oriented programming
- Inheritance and polymorphism
- Properties and encapsulation
- Exception handling and input validation

## Current Limitations

- Employee records are stored in memory and are lost when the application exits.
- Employee salaries and tax rates are currently defined in the employee subclasses.
- The application runs entirely in the terminal and has no graphical interface or database integration.

## Future Improvements

- Add JSON or database persistence.
- Improve employee record management and validation.
- Add automated tests for salary calculations and input handling.
- Separate classes, functions, and application logic into modules.
