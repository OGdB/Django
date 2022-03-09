class AccountError(Exception):
    def __init__(self, reason):
        super().__init__(reason)

class Account:
    def __init__(self, uname, pwd):
        self.username = uname
        self.password = pwd

accounts = {}

def addAccount(email, pwd):
    """Add account to accounts, if the input was valid"""
    if not isinstance(email, str) or len(email.strip()) <= 0: # no username
        raise AccountError("Must enter a username!")
    if not isinstance(pwd, str) or len(pwd.strip()) <= 0: # no password
        raise AccountError("Must enter a password!")
        
    # if valid input:
        # look for 1 @ sign:
            # string of input on left of @,
            # string of input on right of @,
            # require exactly 1 . which must be on right side of @,
            # must be at least one character between @ and dot,
            # must be at least one character after dot.
    if email.count("@") == 1:
        ulist = email.split("@")
        username = ulist[0]
        domain = ulist[1]
        ds = domain.rsplit(".")  # split right side of @ at last dot.
        domain_address = ds[0]
        domain_type = ds[1]

        # if valid e-mail e.g: 'foo@foomail.fong'
        if not (len(username) > 0 and len(domain_address) > 0 and len(domain_type) > 0):
            raise AccountError("Invalid e-mail address entered!")
    else:
        raise AccountError("Must enter valid e-mail address with one @-sign!")

    if email in accounts:
        raise AccountError("Username already exists!")

    u = Account(email, pwd)
    accounts[email]=u

def verifyUser(uname, pwd):
    """Return whether username exists and password is correct"""
    if uname in accounts:
        this_account = accounts[uname]
        return this_account.password == pwd
    else:
        return False

def clear():
    global accounts
    accounts = {}