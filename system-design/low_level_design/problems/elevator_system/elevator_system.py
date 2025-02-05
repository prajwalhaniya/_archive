from typing import List

class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)

        return cls._instance


@dataclass
class ElevatorSystem(Singleton):
    building

    def monitoring(self):
        pass

    def dispatcher(self):
        pass


@dataclass
class Building(Singleton):
    floors: List
    elevators: List