class Reservation(object):
    def __init__(self, id : int, user, show, price : float, seat : str, type : str ) -> None:
        self.ID = id
        self.UserObj = user
        self.ShowObjt = show
        self.Price = price
        self.SeatNumber = seat
        self.Type = type
