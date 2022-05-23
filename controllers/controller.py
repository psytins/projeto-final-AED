import models.reservation as reservation
import models.show as show
import models.user as user
import models.model as model
import json

def start():
    #Associar a listas globais para cada objeto
    model.User_List = list()
    model.Show_List = list()
    model.Reservation_List = list()
    #Adicionar elementos do user.json para uma array de objetos
    f_users = open('./data/users.json')
    data_users = json.load(f_users)
    for u in data_users:
        temp_user = user.User(u["ID"],u["Full Name"],u["Email"],u["Password"],u["Admin"])
        model.User_List.append(temp_user)
        temp_user = None
    f_users.close()
    #Adicionar elementos do shows.json para uma array de objetos
    f_shows = open('./data/shows.json')
    data_shows = json.load(f_shows)
    for s in data_shows:
        temp_shows = show.Show(s["ID"],s["Show Name"],s["Date"],s["Capacity"],s["Description"],s["Room"])
        model.Show_List.append(temp_shows)
        temp_shows = None
    f_shows.close()
    #Adicionar elementos do reservation.json para um array de objetos
    f_reservations = open('./data/reservations.json')
    data_reservations = json.load(f_reservations)
    for r in data_reservations:
        temp_reservations = reservation.Reservation(r["ID"],r["User ID"],r["Username"],r["Show ID"],r["Show Name"],r["Type"],r["Price"],r["Seat Number"])
        model.Reservation_List.append(temp_reservations)
        temp_reservations = None
    f_reservations.close()

def save():
    model.User_List = list()        #temp
    model.Reservation_List = list() #temp
    model.Show_List = list()        #temp
    # --------------
    # pegar na lista de objectos (objeto em json -> dict em python)
    # converter cada objecto num objecto python-json 
    # dump para tranformar num objecto json
    # file write
    # --------------
    #For users
    user_json = list()
    for users in model.User_List:
        temp_dict_users = dict()
        temp_dict_users["ID"] = users.getID()
        temp_dict_users["Full Name"] = users.getFullName()
        temp_dict_users["Email"] = users.getEmail()
        temp_dict_users["Password"] = users.getPassword()
        temp_dict_users["Admin"] = users.isAdmin()
        user_json.append(temp_dict_users)
    load_json = json.dumps(user_json)
    #Write in json file
    with open("./data/test_user.json","w") as file:
        file.write(load_json)
        file.close()
        