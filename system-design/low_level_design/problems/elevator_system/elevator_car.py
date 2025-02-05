from dataclasses import dataclass


@dataclass
class ElevatorCar:
    __id
    door
    state
    display
    panel

    def move(self):
        pass

    def stop(self):
        pass
