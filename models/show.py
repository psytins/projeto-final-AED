class Show(object):
    def __init__(self, id : int, name : str, date : str, capacity : bool, description : str, room : list) -> None:
        self.id = id
        self.show_name = name
        self.date = date
        self.capacity = capacity
        self.description = description
        self.room = room
    
    def getID(self):
        return self.id

    def getShowName(self):
        return self.show_name

    def getDate(self):
        return self.date

    def getCapacity(self):
        return self.capacity

    def getDescription(self):
        return self.description

    def getRoom(self):
        return self.room

    def getSeatNumber(self,room_index : tuple):
        pass