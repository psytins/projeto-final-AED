from tkinter.messagebox import RETRY


class Show(object):
    def __init__(self, id : int, name : str, date : str, description : str, room : list) -> None:
        self.id = id
        self.show_name = name
        self.date = date
        self.description = description
        self.room = room
    
    def getID(self):
        return self.id

    def getShowName(self):
        return self.show_name

    def getDate(self):
        return self.date

    def getCapacity(self):
        if(self.getSeatCount() == 142): return True
        else: return False

    def getDescription(self):
        return self.description

    def getRoom(self):
        return self.room

    def getSeatNumber(self,room_index : tuple):
        pass

    def getSeatCount(self):
        counter = 0
        for seats_l in self.room:
            for seats_c in seats_l:
                if(seats_c == "N1" or seats_c == "v1"):
                    counter += 1
        return counter
