import models.reservation as reservation
import models.show as show
import models.user as user
import json

def start():
    # pegar no ficheiro json 
    # converter para um objeto json em python
    # converter objeto json para um objeto nosso 
    # esse objeto, dar append na lista
    # lista = [obj1, obj2, obj3, ...]
    f_users = open('./data/users.json')
    data = json.load(f_users)
    