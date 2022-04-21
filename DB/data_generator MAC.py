#The purpose of this program will be to create simulated data for our machine learning. 
import random
import requests
import os
from datetime import datetime
import math
import weather_input
import copy

class item:
    def __init__(self, name, min, max, deviation, id, ival):
        self.name = name
        self.min = min
        self.max = max
        self.dev = deviation
        self.orders = []
        self.id = id
        self.init_val = ival
        self.store_avg = 0
        self.shipped = False
        self.shipping_time = 2
        self.two_week_grace = 0
        self.holiday_mod = 2
        self.weekend_mod = 0
#init the obj array for the items
item_list = []
holiday = [1, 45, 76, 104, 129, 171, 213, 214, 215, 216, 217, 218, 219, 
            220, 221, 222, 223, 224, 225, 226, 227, 228, 229 , 230, 304,
            331, 338, 345, 352, 353, 355, 356, 357, 360]
#this will pull the most current list from my git
url = "https://raw.githubusercontent.com/jgthornb/files/main/item_generation.txt"
page = requests.get(url)
local_file = 'item_copy.txt'
#saves a copy to the current folder. can be deleted later. 
with open(local_file, 'wb') as file:
    file.write(page.content)
#read the file and put the obj in to the array
fname = os.getcwd() + '//' + local_file
def fill_list():
    with open(fname, "r") as myfile:
        for line in myfile:
            x = line.strip().split(", ")           
            item_list.append(item(x[0], int(x[1]), int(x[2]), int(x[3]), x[4], int(x[5])))
    for i in range(len(item_list)):        
        get_item_avg(item_list[i])        
        item_list[i].two_week_grace = item_list[i].store_avg * 14

#prints out a specific object
def get_item_avg(self):
    self.store_avg = (random.randrange(self.min, self.max, 1))

def print_obj(self):
    print(self.name, self.min, self.max, self.dev, self.id, self.init_val)

def decrease_stock(self, item_use, day):    
    self.init_val -= math.floor(item_use * self.weekend_mod)
    if self.init_val <= 0 and self.shipped == False:
        emergency_order(self, day)        
    if self.init_val < (self.store_avg * self.shipping_time) and self.shipped == False:       
        self.shipped = True 
        #self.orders.append([day, self.init_val, item_use]) 
        self.orders.append([day])             

def need_ordering(self):
    if self.shipped == True:
        self.shipping_time -= 1       

def resupply_stock(self):
    if self.shipping_time == 0:
        self.init_val += self.two_week_grace
        self.shipping_time = 2
        self.shipped = False

def weekend_check(self, day):
    day_check = day % 7
    if day_check >= 4:
        self.weekend_mod = (1 + ((day_check * 10)/100))
    elif day_check <= 1:
        self.weekend_mod = (1 - ((day_check * .5)/100)) 
    else:
        self.weekend_mod = 1

def emergency_order(self, day):    
    self.shipped = True
    self.init_val = 0
    self.shipping_time = 1

def the_loop():
    weather_input.execute()
    #copies the weather list from weather_input and makes it a bit easier to use here
    #use weather_cpy when looping for the weather data 
    #but, i may change this up. so a test of the deepcopy library
    weather_cpy = copy.deepcopy(weather_input.weather_list) 
    print(weather_cpy[34].temp_avg) 
    for j in range(len(item_list)):
        holiday_incr = 0
        for i in range(365):
            #see if there is a holiday coming up
            #check for weather event  
            #this is where we will make modifications to the avg
            mod_avg = item_list[j].store_avg
            if i == holiday[holiday_incr]:              
                mod_avg = mod_avg * item_list[j].holiday_mod               
                holiday_incr = (holiday_incr + 1) %  len(holiday)
            resupply_stock(item_list[j])
            weekend_check(item_list[j], i)            
            decrease_stock(item_list[j], mod_avg, i)
            need_ordering(item_list[j])
            

def file_check():
    mydir = ("output-data-gen")
    check_folder = os.path.isdir(mydir)
    if not check_folder:
        os.makedirs(mydir)

def save_doc():
    now = datetime.now()
    file_check()
    f = open(os.getcwd() + "/output-data-gen/data-gen-"+ now.strftime("%H-%M-%S") +".txt", 'w+')
    for i in range(len(item_list)):
        f.write(str(item_list[i].name) + " " + str(item_list[i].orders) + "\n")
    f.close()
    
#what initiates all the work    
def execute():           
    fill_list()
    the_loop()
    print(item_list[5].orders)
    save_doc()

execute()