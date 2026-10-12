employee_payroll_data = {}

def get_text(prompt):
    """Keep asking until the user enters a non-empty value."""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Input cannot be empty. Please try again.")


def get_int(prompt, min_value=None):
    """Keep asking until the user enters a whole number (optionally >= min_value)."""
    while True:
        value = input(prompt).strip()
        try:
            number = int(value)
        except ValueError:
            print("Invalid input. Please enter a whole number.")
            continue
        if min_value is not None and number < min_value:
            print(f"Please enter a number that is {min_value} or greater.")
            continue
        return number


def get_category(prompt):
    """Keep asking until the user enters 1, 2 or 3."""
    while True:
        value = input(prompt).strip()
        if value in ("1", "2", "3"):
            return value
        print("Invalid category. Please enter 1, 2 or 3.")


def get_account_number(prompt):
    """Keep asking until the user enters a numeric account number."""
    while True:
        value = input(prompt).strip()
        if value.isdigit():
            return value
        print("Invalid account number. Please enter digits only.")
