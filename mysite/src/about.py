from django.shortcuts import render
import time

def view(req):
    ctx = {
        "name" : "Bob",
        "now" : time.asctime()
    }
    return render( req, "about.html", ctx )