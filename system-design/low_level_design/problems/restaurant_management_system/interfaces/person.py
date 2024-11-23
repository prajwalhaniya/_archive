
from abc import ABC

class Person(ABC):
    def __init__(self, name, email, phone_number):
        self.__name = name
        self.__email = email
        self.__phone_number = phone_number

class Customer(Person):
    def __init__(self, name, email, phone_number, last_visited_date):
        super().__init__(name, email, phone_number)
        self.__last_visited_date = last_visited_date

class Employee(Person):
    def __init__(self, name, email, phone_number, employee_id, joining_date):
        super.__init__(name, email, phone_number)
        self.__employee_id = employee_id
        self.__joining_date = joining_date

class Chef(Employee):
    def prepare_order():
        pass

class Waiter(Employee):
    def take_order():
        pass

class Manager(Employee):
    def add_employee():
        pass

class Receptionist(Employee):
    def create_reservation():
        pass