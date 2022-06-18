class Reservation(object):
    def __init__(self, id : int, user_id : int, user_name : str, show_id : int, show_name : str, price : float, seat : str, seat_type : str ) -> None:
        self.id = id
        self.user_id = user_id
        self.user_name = user_name
        self.show_id = show_id
        self.show_name = show_name
        self.price = price
        self.seat_number = seat
        self.show_type = seat_type

    def getID(self):
        return self.id

    def getUserID(self):
        return self.user_id

    def getUserName(self):
        return self.user_name

    def getShowID(self):
        return self.show_id

    def getShowName(self):
        return self.show_name

    def getPrice(self):
        return format(float(self.price), '.2f')

    def getSeatNumber(self):
        return self.seat_number

    def getSeatType(self):
        return self.show_type