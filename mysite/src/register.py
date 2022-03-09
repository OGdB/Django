import django.http
import django.views.decorators.csrf
import src.AccountManager as AccountManager

#@django.views.decorators.csrf.csrf_exempt
def register(req):
    # is this a host request?
    if req.method != "POST":
        return django.http.HttpResponseBadRequest("Must use POST")
    uname = req.POST.get("username")
    pwd = req.POST.get("password")
    
    try:
        if uname not in AccountManager.accounts:
            AccountManager.addAccount(uname, pwd)
            req.session["user"]=uname 
            req.session.modified = True # tell Django to update session data
            return django.http.HttpResponse("OK")
        else:
            raise AccountManager.AccountError("Username already in use!")

    except AccountManager.AccountError as e:
        return django.http.HttpResponseBadRequest()
