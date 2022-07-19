from dataclasses import dataclass


@dataclass
class Person:

    full_name: str = None
    first_name: str = None
    last_name: str = None
    email: str = None
    current_address: str = None
    permanent_address: str = None
    age: int = None
    salary: int = None
    department: str = None


class PersonInfo(Person):
    def __init__(self, first_name, last_name, email, age, salary, department):
        self.full_name = first_name + " " + last_name
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.salary = salary
        self.age = age
        self.department = department