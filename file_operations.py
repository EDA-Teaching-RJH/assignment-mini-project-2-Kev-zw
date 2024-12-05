import csv

def write_csv(file_path, data):
    """Write data to a file"""
    with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

def read_csv(file_path):
    """Read data from the file."""
    with open(file_path, mode='r') as file:
        reader = csv.reader(file)
        return [row for row in reader]
