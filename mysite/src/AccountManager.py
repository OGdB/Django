class AccountManager:
    def __init__(self):
        self.users = {}

    def addUser(self, uname, passwd):
        if uname in self.users:
            return False
        self.users[uname] = passwd
        return True

    def verifyUser(self, uname, passwd):
        if uname in self.users:
            return self.users[uname]==passwd
        else:
            return False
