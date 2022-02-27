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
        AccountManager.addAccount(uname, pwd)
        return django.http.HttpResponse("OK")
        
    except AccountManager.AccountError as e:
        return django.http.HttpResponseBadRequest()
