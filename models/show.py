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

    def getSeatIndex(self,seat_number) -> tuple:
        first = seat_number[0]
        second = int(seat_number[1:])
        seat_letter = ["K","J","I","H","G","F","E","D","C","B","A"]
        first_index = seat_letter.index(first)
        second_index = second - 1
        return (first_index,second_index)

    def getSeatNumber(self, seat_index : tuple):
        first = seat_index[0]
        second = seat_index[1]
        seat_letter = ["K","J","I","H","G","F","E","D","C","B","A"]
        return seat_letter[first] + str(second+1)

    def getSeatType(self,seat_number):
        seat_index = self.getSeatIndex(seat_number)
        if(self.room[seat_index[0]][seat_index[1]] == "N0" or self.room[seat_index[0]][seat_index[1]] == "N1"):
            return "NORMAL"
        elif(self.room[seat_index[0]][seat_index[1]] == "V0" or self.room[seat_index[0]][seat_index[1]] == "V1"):
            return "VIP"

    def getPriceFromSeat(self,seat_number): #Preços estipulados para cada espetáculo
        if(self.getSeatType(seat_number) == "NORMAL"):
            return 4.00
        elif(self.getSeatType(seat_number) == "VIP"):
            return 12.00

    def getSeatCount(self):
        counter = 0
        for seats_l in self.room:
            for seats_c in seats_l:
                if(seats_c == "N1" or seats_c == "V1"):
                    counter += 1
        return counter
    
    def setSeatOccupancy(self,seat_number,taken : bool):
        seat_index = self.getSeatIndex(seat_number) #tuple
        if(taken):
            if(self.getSeatType(seat_number) == "NORMAL"): self.room[seat_index[0]][seat_index[1]] = "N1"
            elif(self.getSeatType(seat_number) == "VIP"): self.room[seat_index[0]][seat_index[1]] = "V1"
        else:
            if(self.getSeatType(seat_number) == "NORMAL"): self.room[seat_index[0]][seat_index[1]] = "N0"
            elif(self.getSeatType(seat_number) == "VIP"): self.room[seat_index[0]][seat_index[1]] = "V0"
