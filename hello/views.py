#from django.urls import reverse
import requests
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
import subprocess
import webbrowser
import os
import glob
  
from hello.test12 import runArray

from .models import Greeting

#url = "https://raw.githubusercontent.com/gwromano/predictiveplanning/main/run.sh?token=GHSAT0AAAAAABTGWQ3KHPYS6IEIBLFQ67REYTBOZNA"

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def index(request):
    #return HttpResponse('Hello from Python!')
    # r = requests.get('https://httpbin.org/status/418')
    # print(r.text)
    # return HttpResponse('<pre>' + r.text + '</pre>')
    # if "makeOrder" in request.POST:
    #     #return HttpResponseRedirect(".")
    #     return render(request, "about-us.html")
    #if request.method == 'POST' and 'run_script' in request.POST:
        #runArray()
        
    return render(request, "index.html")

def makeOrder(request):
    if request.POST:    
        #url = "https://raw.githubusercontent.com/maggieturner/Capstone/main/run.sh?token=GHSAT0AAAAAABTGWQ3K73MIRHTSPRXQWCDWYTBRGSA"
        #webbrowser.open_new(url)
        #subprocess.call(url)
        #subprocess.call('/Users/maggieturner/Documents/Github/Capstone/run.sh') #maggie path
        #subprocess.call(['open', '-W', '-a', 'Terminal.app', 'python', '--args', 'test12.py'])
        subprocess.call('start /wait run.sh', shell=True) #george
        #subprocess.run(['run.sh'])
        #subprocess.run(['python', 'data_gen_mk2.py'])
        #subprocess.call(r'C:\Users\georg\OneDrive\Documents\Visual Studio Projects\predictiveplanning\run.sh', shell=True) #george path
        #subprocess.Popen([r"/Users/maggieturner/Documents/Github/Capstone/run.sh", "https://raw.githubusercontent.com/maggieturner/Capstone/main/run.sh?token=GHSAT0AAAAAABTGWQ3LOSDTEW3D6EMPFEUCYTBQ2SA"])
    return render(request, "make-order.html")
    #return render(request, "about-us.html")

def orderHistory(request):
    if request.POST and 'pdf1' in request.POST:
        webbrowser.open(BASE_DIR + "\ML" + "\Three Pass Graphs" + "\Item_blank badges_.csv.pdf") 
    elif 'pdf2' in request.POST: 
        webbrowser.open(BASE_DIR + "\ML" + "\Three Pass Graphs" + "\Item_box cutters_.csv.pdf")  
    elif 'pdf3' in request.POST:
        webbrowser.open(BASE_DIR + "\ML" + "\Three Pass Graphs" + "\Item_cleaner_.csv.pdf")  
    elif 'pdf4' in request.POST:
        webbrowser.open(BASE_DIR + "\ML" + "\Three Pass Graphs" + "\Item_keyboards_.csv.pdf") 
    elif 'pdf5' in request.POST:
        webbrowser.open(BASE_DIR + "\ML" + "\Three Pass Graphs" + "\Item_light bulbs_.csv.pdf")  
    elif 'pdf6' in request.POST:
        webbrowser.open(BASE_DIR + "\ML" + "\Three Pass Graphs" + "\Item_meat trays_.csv.pdf")  
    elif 'pdf7' in request.POST:
        webbrowser.open(BASE_DIR + "\ML" + "\Three Pass Graphs" + "\Item_office chair_.csv.pdf")  
    elif 'pdf8' in request.POST:
        webbrowser.open(BASE_DIR + "\ML" + "\Three Pass Graphs" + "\Item_paper towel_.csv.pdf")  
    elif 'pdf9' in request.POST:
        webbrowser.open(BASE_DIR + "\ML" + "\Three Pass Graphs" + "\Item_pens_.csv.pdf")  
    elif 'pdf10' in request.POST:
        webbrowser.open(BASE_DIR + "\ML" + "\Three Pass Graphs" + "\Item_photo paper_.csv.pdf") 
    elif 'pdf11' in request.POST:
        webbrowser.open(BASE_DIR + "\ML" + "\Three Pass Graphs" + "\Item_plastic bags_.csv.pdf")   
    elif 'pdf12' in request.POST:
        webbrowser.open(BASE_DIR + "\ML" + "\Three Pass Graphs" + "\Item_plastic wrap_.csv.pdf")  
    elif 'pdf13' in request.POST:
        webbrowser.open(BASE_DIR + "\ML" + "\Three Pass Graphs" + "\Item_printer paper_.csv.pdf")  
    elif 'pdf14' in request.POST:
        webbrowser.open(BASE_DIR + "\ML" + "\Three Pass Graphs" + "\Item_produce bags_.csv.pdf")  
    elif 'pdf15' in request.POST:
        webbrowser.open(BASE_DIR + "\ML" + "\Three Pass Graphs" + "\Item_scanner batt_.csv.pdf")  
    elif 'pdf16' in request.POST:
        webbrowser.open(BASE_DIR + "\ML" + "\Three Pass Graphs" + "\Item_soap_.csv.pdf")  
    elif 'pdf17' in request.POST:
        webbrowser.open(BASE_DIR + "\ML" + "\Three Pass Graphs" + "\Item_toilet paper_.csv.pdf") 
    elif 'pdf18' in request.POST:
        webbrowser.open(BASE_DIR + "\ML" + "\Three Pass Graphs" + "\Item_water bottles_.csv.pdf")   
    elif 'pdf19' in request.POST:
        webbrowser.open(BASE_DIR + "\ML" + "\Three Pass Graphs" + "\Item_wrenches_.csv.pdf")  
        #for file in glob.glob("ML\Three Pass Graphs\*.pdf"):
            #os.startfile(file)
        #webbrowser.open()


    return render(request, "order-history.html")

def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})
