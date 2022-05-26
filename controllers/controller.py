import models.reservation as reservation
import models.show as show
import models.user as user
import models.model as model
import json
#Função utilizada quando se dá o início do programa
#Esta função vai carrregar todos os dados dos JSON nas variáveis globais do tipo lista (ver no models/model)
def start():
    #Associar a listas globais para cada objeto
    model.User_List = list()
    model.Show_List = list()
    model.Reservation_List = list()
    #Adicionar elementos do user.json para uma array de objetos
    f_users = open('./data/users.json',encoding="utf-8")
    data_users = json.load(f_users)
    for u in data_users:
        temp_user = user.User(u["ID"],u["Full Name"],u["Email"],u["Password"],u["Admin"])
        model.User_List.append(temp_user)
        temp_user = None
    f_users.close()
    #Adicionar elementos do shows.json para uma array de objetos
    f_shows = open('./data/shows.json',encoding="utf-8")
    data_shows = json.load(f_shows)
    for s in data_shows:
        temp_shows = show.Show(s["ID"],s["Show Name"],s["Date"],s["Capacity"],s["Description"],s["Room"])
        model.Show_List.append(temp_shows)
        temp_shows = None
    f_shows.close()
    #Adicionar elementos do reservation.json para um array de objetos
    f_reservations = open('./data/reservations.json',encoding="utf-8")
    data_reservations = json.load(f_reservations)
    for r in data_reservations:
        temp_reservations = reservation.Reservation(r["ID"],r["User ID"],r["User Name"],r["Show ID"],r["Show Name"],r["Price"],r["Seat Number"],r["Type"])
        model.Reservation_List.append(temp_reservations)
        temp_reservations = None
    f_reservations.close()
#Função utilizada quando se termina o programa
#Esta função vai carrregar todos os dados das listas globais (model) nos ficheiros JSON
def save():
    # --------------
    # pegar na lista de objectos (objeto em json -> dict em python)
    # converter cada objecto num objecto python-json 
    # dump para tranformar num objecto json
    # file write
    # --------------
    #Save in JSON - For users
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
    with open("./data/users.json","w") as file:
        file.write(load_json)
        file.close()
    #######################################################
    #Save in JSON - For shows
    show_json = list()
    for shows in model.Show_List:
        temp_dict_shows = dict()
        temp_dict_shows["ID"] = shows.getID()
        temp_dict_shows["Show Name"] = shows.getShowName()
        temp_dict_shows["Date"] = shows.getDate()
        temp_dict_shows["Capacity"] = shows.getCapacity() 
        temp_dict_shows["Description"] = shows.getDescription()
        temp_dict_shows["Room"] = shows.getRoom()
        show_json.append(temp_dict_shows)
    load_json = json.dumps(show_json)
    #Write in json file
    with open("./data/shows.json","w") as file:
        file.write(load_json)
        file.close()       
    #######################################################
    #Save in JSON - For reservation
    reservation_json = list()
    for reservations in model.Reservation_List:
        temp_dict_reservations = dict()
        temp_dict_reservations["ID"] = reservations.getID()
        temp_dict_reservations["User ID"] = reservations.getUserID()
        temp_dict_reservations["User Name"] = reservations.getUserName()
        temp_dict_reservations["Show ID"] = reservations.getShowID()
        temp_dict_reservations["Show Name"] = reservations.getShowName()
        temp_dict_reservations["Type"] = reservations.getSeatType()
        temp_dict_reservations["Price"] = reservations.getPrice()
        temp_dict_reservations["Seat Number"] = reservations.getSeatNumber()
        reservation_json.append(temp_dict_reservations)
    load_json = json.dumps(reservation_json)
    #Write in json file
    with open("./data/reservations.json","w") as file:
        file.write(load_json)
        file.close()

#Esta função vai retornar ids que não existam registados para novos registos
def create_id():
    tmp_verify = []
    id_verify = 20000
    #adicionei os ids existentes a uma lista temporaria
    for x in range(len(model.User_List)):
        tmp_verify.append(model.User_List[x].getID())
    #aqui verifiquei se os ids existiam ou não na lista temporária criada
    if id_verify not in tmp_verify:
        return id_verify
    else:
        for i in range(len(tmp_verify)):
            if id_verify == tmp_verify[i]:
                id_verify += 1
        return id_verify