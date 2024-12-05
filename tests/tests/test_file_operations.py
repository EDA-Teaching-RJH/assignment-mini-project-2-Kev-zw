import unittest
import os
from file_operations import write_csv, read_csv

class TestFileOperations(unittest.TestCase):
    def setUp(self):
        self.file_path = "test_data.csv"
        self.data = [["Name", "Age"], ["Alice", 25], ["Bob", 30]]

    def tearDown(self):
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_write_and_read_csv(self):
        write_csv(self.file_path, self.data)
        read_data = read_csv(self.file_path)
        self.assertEqual(read_data, self.data)

if __name__ == "__main__":
    unittest.main()
