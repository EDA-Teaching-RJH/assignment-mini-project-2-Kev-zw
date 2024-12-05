import re

def extract_emails(text):
    """Extract all email addresses from a given text, then lists them."""
    pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    return re.findall(pattern, text)

def validate_phone_number(phone_number):
    """Validate if the phone number matches a specific pattern."""
    pattern = r"^\+\d{1,3}-\d{3}-\d{4}$"
    return bool(re.match(pattern, phone_number))
