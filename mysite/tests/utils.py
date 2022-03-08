import django.test

def addAccount(uname, pwd):
    c = django.test.Client()
    resp = c.post("/register",
    {
        "username": uname,
        "password":pwd
    }
    )
    return resp