from django.http import HttpResponse

def showHomePage(request):
    return HttpResponse("Hello, world")