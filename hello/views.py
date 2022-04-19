#from django.urls import reverse
import requests
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect

from hello.test12 import runArray

from .models import Greeting

# Create your views here.
def index(request):
    #return HttpResponse('Hello from Python!')
    # r = requests.get('https://httpbin.org/status/418')
    # print(r.text)
    # return HttpResponse('<pre>' + r.text + '</pre>')
    # if "makeOrder" in request.POST:
    #     #return HttpResponseRedirect(".")
    #     return render(request, "about-us.html")
    if request.method == 'POST' and 'run_script' in request.POST:
        runArray()
        
    return render(request, "index.html")



def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})
