class Table:
    def __init__(self, table_id, status, max_capacity, location_identifier, seats):
        self.__table_id = table_id
        self.__status = status
        self.__max_capacity = max_capacity
        self.__location_identifier = location_identifier
        slef.__seats = []

    def is_table_free(self):
        pass

    def add_reservation(self):
        pass

    def search(self):
        pass


class TableSeat:
    def __init__(self, table_seat_number, typee):
        self.__table_seat_number = table_seat_number
        self.__typee = typee

    def update_seat_type(self, typee):
        pass


