from app_enums import ReservationStatus

class Reservation:
    def __init__(self, id, people_count, notes, customer):
        self.__reservation_id = id
        self.__time_of_reservation = datetime.datetime.now()
        self.__people_count = people_count
        self.__status = ReservationStatus.Requested
        self.__notes = notes
        self.__checkin_time = checkin_time
        self.__customer = customer
        self.__tables = []
        self.__notifications = []

    def update_people_count(self, count):
        None

