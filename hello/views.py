from django import apps
import requests
from django.shortcuts import render
from django.http import HttpResponse


from .models import Greeting

# Create your views here.
@apps.route("/index.html", methods=["GET","POST"])
def index(request):
    method = request.method
    #return HttpResponse('Hello from Python!')
    # r = requests.get('https://httpbin.org/status/418')
    # print(r.text)
    # return HttpResponse('<pre>' + r.text + '</pre>')
    #return render(request, "index.html")
    return render("index.html", method=method)


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})
