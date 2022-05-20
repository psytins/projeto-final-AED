class User(object):
    def __init__(self, id : int, name : str, email : str, password : str, is_admin : bool) -> None:
        self.ID = id
        self.FullName = name
        self.Email = email
        self.Password = password
        self.Admin = is_admin
    
    def getID(self):
        return self.ID
    
    def getFullName(self):
        return self.FullName