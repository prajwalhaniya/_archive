## Enumerations and custom data type

```python
# Enumeration
class PaymentStatus(Enum):
    COMPLETED = 1
    FAILED = 2
    PENDING = 3
    UNPAID = 4
    REFUNDED = 5
    
class AccountStatus(Enum):
		ACTIVE = 1
		CLOSED = 2
		CANCELED = 3
		BLACKLISTED = 4
		NONE = 5
		
# data types
class Person:
		def __init__(self, name, address, phone, email):
				self.__name = name
				self.__address = address
				self.__phone = phone
				self.__email = email
				
class Address:
		def __init__(self, zip_code, address, city, state, country):
				self.__zip_code = zip_code
				self.__address = address
				self.__city = city
				self.__state = state
				self.__country = country

```

## Parking spots

The first section of the parking lot system that we will work on is the `ParkingSpot` class, which will act as a base class for four different types of parking spots: handicapped, compact, large, and motorcycle. This will have an instance of the `Vehicle` class. The definition of the `ParkingSpot` class and the classes being derived from it are given below:

```python
from abc import ABC, abstracmethod

def ParkingSpot(ABC):
    def __init__(slef, id, isFree, vehicle):
				self.__id = id
				self.__isFree = isFree
				self.__vehicle = vehcle
				
		def get_is_free(self):
				pass
		
		@abstractmethod
		def assign_vehicle(self, vehicle):
				pass
				
		def remove_vehicle(self):
				pass
				
class Handicapped(ParkingSpot):
		def __init__(self, id, isFree, vehicle):
				super().__init__(id, isFree, vehicle)
				
		def assign_vehicle(self, vehicle):
				pass
				
# similarly write other classes for Compact, Large, Motorcycle vehicles

```

## Vehicle

`Vehicle` will be another abstract class, which serves as a parent for four different types of vehicles: car, truck, van, and motor cycle. The definition of the `Vehicle` and its child classes are given below:

```python
from abc import ABC, abstractmethod

class Vehicle(ABC):
		def __init__(self, license_no):
				self.__license_no = license_no
				
		@abstractmethod
		def assign_ticket(self, ticket):
				pass
				
class Car(Vehicle):
		def __init__(self, license_no):
				super().__init__(license_no)
				
		def assign_ticket(self, ticket):
				pass
				
# similarly write other classes for Van, Truck, and MotorCycle
```

## Account

The `Account` class will be an abstract class, which will have the actors, `Admin` and `ParkingAttendant`, as child classes. The definition of these classes is given below:

```python
from abc import ABC, abstractmethod

class Account(ABC):
		def __init__(self, user_name, password, person, status):
				self.__user_name = user_name
				self.__password = password
				self.__person = person
				self.__status = status
				
				
		@abstractmethod
		def reset_password(self):
				pass
	
class Admin(Account):
		def __init__(self, user_name, password, person, status):
				super().__init_(user_name, password, person, status)
				
		def add_parking_spot(self, spot)
			pass
			
		def add_display_board(self, display_board):
				pass
				
		def add_entrance(self, entrance):
				pass
				
		def add_exit(self, exit):
				pass
				
		def reset_password(self):
				pass
				
class ParkingAttendent(Account):
		def __init__(self, user_name, password, person, status):
				super().__init_(user_name, password, person, status)
				
		def process_ticket(self, ticket_number):
				pass
				
		def reset_password(self):
				pass	
```

## Display board and parking rate

This section contains the `DisplayBoard` and `ParkingRate` classes that only have the composition class with the `ParkingLot` class. This relationship is highlighted in the `ParkingLot` class. The definition of these classes is given below:

```python
class DisplayBoard:
		def __init__(self, id):
				self.__id = id
				self.__parking_spots = {}
				
		def add_parking_spot(self, spot_type, spots):
				pass
		
		def show_free_slot(self):
				pass
				
class ParkinRate:
		def __init__(self, hours, rate):
				self.__hours = hours
				self.__rate = rate
				
		def calculate(self):
				pass
				
```

## Entrance and exit

This section contains the `Entrance` and `Exit` classes, both of which are associated with the `ParkingTicket` class. The definition of the `Entrance` and `Exit` classes is given below:

```python
class Entrance:
		def __init__(self, id, ticket):
				self.__id = id
				
		def get_ticket(self):
				pass
				
class Exit:
		def __init__(self, id, ticket):
				self.__id = id
				
		def validate_ticket(self, ticket):
				pass
```

## Parking ticket

The definition of the `ParkingTicket` class can be found below. This contains instancesof the `Vehicle`, `Payment`, `Entrance` and `Exit` classes:

```python
class ParkingTicket:
		def __init__(
				self,
				ticket_no,
				timestamp,
				exit,
				amount,
				status,
				vehicle,
				payment,
				entrance,
				exit_ins		
		):
				self.__ticket_no = ticket_no
				self.__timestamp = timestamp
				self.__exit = exit
				self.__amount = amount
				self.__status = status
				
				# following are the instances of the respective classes
				
				self__vehicle = vehicle
				self__payment = payment
				self__entrance = entrance
				self__exit_ins = exit_ins
```

## Payment

The `Payment` class is another abstract class, with the `Cash` and `CreditCard` classes as its child. This takes the `PaymentStatus` enumeration and the `dateTime` data type to keep track of the `payment status` and time. The definition of this class is given below

```python
from abc import ABC, abstractmethod

class Payment(ABC):
		def __init__(self, amount, status, timestamp):
				self.__amount = amount
				self.__status = status
				self.__timestamp = timestamp
				
		@abstractmethod
		def initiate_transaction(self):
				pass
				
class Cash(Payment):
		def __init__(self, amount, status, timestamp):
				super().__init__(amount, status, timestamp)
				
		def initiate_transaction(self):
				pass
				
# similarly add class for CreditCard, DebitCard etc			
```

## Parking lot

The final class of the parking lot system is the `ParkingLot` class which will be a Singleton class, meaning the entire system will only have one instance of this class. The definition of this class is given below:

```python
class __ParkingLot(object):
		__instance = None
		
		def __new__(cls):
				if cls.__instances is None:
						cls.__instances = super(__ParkingLot, cls).__new__(cls)
				return cls.__instances
				
class ParkingLot(metaclass=__ParkingLot):
		def __init__(self, id, name, address, parking_rate):
				self.__id = id
				self.__name = name
				self.__address = address
				self.__parking_rate = parking_rate
				
				self.__entrance = {}
				self.__exit = {}
				
				self.__tickets = {}
				
		def add_entrance(self, entrance):
				pass
				
		def add_exit(self, exit):
				pass
				
		def get_parking_ticket(self, vehicle):
				pass
				
		def is_full(self, type):
				pass
```