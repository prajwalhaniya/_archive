class MealItem:
    def __init__(self, meal_item_id, quantity, menu_item):
        self.__meal_item_id = meal_item_id
        self.__quantity = quantity
        self.__menu_item = menu_item

    def update_quantity(self, quantity):
        pass

class Meal:
    def __init__(self, meal_id, seat, menu_items):
        self.__meal_id = meal_id
        self.__seat = seat
        self.__menu_items = []

    def add_meal_item(self, meal_item):
        pass


