class Reservation(object):
    def __init__(self, id : int, user_id : int, user_name : str, show_id : int, show_name : str, price : float, seat : str, type : str ) -> None:
        self.id = id
        self.user_id = user_id
        self.user_name = user_name
        self.show_id = show_id
        self.show_name = show_name
        self.price = price
        self.seat_number = seat
        self.type = type

    def getID(self):
        return self.id

    def getUserID(self):
        return self.user_id

    def getUserName(self):
        return self.user_name

    def GetShowID(self):
        return self.show_id

    def GetName(self):
        return self.show_name

    def GetPrice(self):
        return self.price

    def GetSeatNumber(self):
        return self.seat_number

    def GetType(self):
        return self.type
