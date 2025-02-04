from enum import Enum

class ElevatorState(Enum):
    IDLE = 1
    UP = 2
    DOWN = 3

class Direction(Enum):
    UP = 1
    DOWN = 2

class DoorState(Enum):
    OPEN = 1
    CLOSE = 2