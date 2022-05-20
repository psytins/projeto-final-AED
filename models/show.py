class Show(object):
    def __init__(self, id : int, name : str, date : str, capacity : bool, description : str, room : list) -> None:
        self.ID = id
        self.ShowName = name
        self.Date = date
        self.Capacity = capacity
        self.Description = description
        self.Room = room

    def getSeatNumber(self,room_index : tuple):
        pass