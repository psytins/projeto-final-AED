class User(object):
    def __init__(self, id : int, name : str, email : str, password : str, is_admin : bool) -> None:
        self.id = id
        self.fullname = name
        self.email = email
        self.password = password
        self.admin = is_admin
    
    def getID(self):
        return self.id
    
    def getFullName(self):
        return self.fullname

    def getEmail(self):
        return self.email

    def getPassword(self):
        return self.password

    def isAdmin(self):
        return self.admin