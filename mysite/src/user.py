import django.http

def getuser(req):
    u = req.session.get("user", "")
    return django.http.HttpResponse(u)  # return empty string