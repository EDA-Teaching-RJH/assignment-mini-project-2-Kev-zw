class Person:
    """Representing a person."""
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"My name is {self.name}, and I am {self.age} years old."

class Employee(Person):
    """Representing an employee."""
    def __init__(self, name, age, job_title):
        super().__init__(name, age)
        self.job_title = job_title

    def introduce(self):
        return f"My name is {self.name}, I am {self.age} years old, and I work as a {self.job_title}."
