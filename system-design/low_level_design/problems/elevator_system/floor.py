from dataclasses import dataclass

@dataclass
class Floor:
    display
    panel

    def is_bottom_most(self):
        pass

    def is_top_most(self):
        pass