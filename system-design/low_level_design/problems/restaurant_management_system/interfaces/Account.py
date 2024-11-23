from abc import abstractmethod

class Account:
    def __init__(self, account_id, password, address, status):
        self.__account_id = account_id
        self.__password = password
        self.__address = address
        self.__status = status

    def reset_password(self):
        pass


