from regex_functions import extract_emails, validate_phone_number
from file_operations import read_csv, write_csv
from custom_library.math_utils import add_numbers
from oop_example import Person, Employee
"""Using the functions"""

def main():
    """Regular Expressions Example"""
    text = "Contact us at support@example.com or sales@example.org."
    emails = extract_emails(text)
    print("Extracted Emails:", emails)
    """Using regex for phone number"""
    phone_number = "+123-123-123"
    is_valid_phone = validate_phone_number(phone_number)
    print(f"Is '{phone_number}' a valid phone number? {is_valid_phone}")

    """File I/O Example"""
    data = [["Name", "Age"], ["Alice", 25], ["Bob", 30]]
    write_csv("example_data.csv", data)
    read_data = read_csv("example_data.csv")
    print("Read Data from CSV:", read_data)

    """Using the Custom Library"""
    result = add_numbers(5, 10)
    print("Sum of 5 and 10 using custom library:", result)

    """Another example"""
    alice = Employee("Alice", 25, "Software Engineer")
    print(alice.introduce())

if __name__ == "__main__":
    main()
