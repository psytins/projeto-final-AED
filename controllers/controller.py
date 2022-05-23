import models.reservation as reservation
import models.show as show
import models.user as user
import models.model as model
import json

def start():
    # pegar no ficheiro json 
    # converter para um objeto json em python
    # converter objeto json para um objeto nosso 
    # esse objeto, dar append na lista
    # lista = [obj1, obj2, obj3, ...]
    f_users = open('./data/users.json')
    data = json.load(f_users)
    
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
