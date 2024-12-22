from enum import Enum

class PaymentStatus(Enum):
    Unpaid = 1
    Pending = 2
    Completed = 3
    Failed = 4
    Declined = 5
    Canceled = 6
    Abondoned = 7
    Settling = 8
    Refunded = 9

class TableStatus(Enum):
    Free = 1
    Reserved = 2
    Occupied = 3
    Other = 4

class SeatType(Enum):
    Regular = 1
    Kid = 2
    Accessible = 3
    Other = 4

class AccountStatus(Enum):
    Active = 1
    Closed = 2
    Canceled = 3
    Blacklisted = 4

class OrderStatus(Enum):
    Received = 1
    Preparing = 2
    Complete = 3
    Canceled = 4

class ReservationStatus(Enum):
    Requested = 1
    Pending = 2
    Confirmed = 3
    CheckedIn = 4
    Canceled = 5
    Abandoned = 6 