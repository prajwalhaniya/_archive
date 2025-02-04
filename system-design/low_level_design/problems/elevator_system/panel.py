from dataclasses import dataclass

@dataclass
class ElevatorPanel:
    floor_buttons
    open_button
    close_button


@dataclass
class HallPanel:
    up
    down

