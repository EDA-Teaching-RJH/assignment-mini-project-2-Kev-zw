import unittest
from regex_functions import extract_emails, validate_phone_number

class TestRegexFunctions(unittest.TestCase):
    def test_extract_emails(self):
        text = "Emails: test@example.com, example@gmail.com"
        self.assertEqual(extract_emails(text), ["test@example.com", "example@gmail.com"])

    def test_validate_phone_number(self):
        self.assertTrue(validate_phone_number("+123-456-7890"))
        self.assertFalse(validate_phone_number("123-456-7890"))

if __name__ == "__main__":
    unittest.main()
