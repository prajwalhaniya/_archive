from abc import ABC, abstractmethod
from dataclasses import dataclass

@dataclass
class Button(ABC):
    status

    def press_down(self):
        pass

    @abstractmethod
    def is_pressed(self):
        pass
    

@dataclass
class HallButton(Button):
    button_sign

    def is_pressed(self):
        pass


@dataclass
class ElevatorButton(Button):
    destination_floor_number

    def is_pressed(self):
        pass