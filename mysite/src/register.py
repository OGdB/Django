import django.http
import django.views.decorators.csrf

@django.views.decorators.csrf.csrf_exempt
def register(req):
    #return django.http.HttpResponseServerError()
    return django.http.HttpResponse("OK")