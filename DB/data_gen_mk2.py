#The purpose of this program will be to create simulated data for our machine learning. 
#from heapq import merge
import random
import requests
import os
from datetime import datetime, date, timedelta
import math
import weather_input
import copy
from xlwt import Workbook
import pandas as pd
import glob
import csvsplitter

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

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
        self.rolling_avg = []
class order:
    def __init__(self, name, day, qty, num):
        self.item_name = name
        self.day = day 
        self.qty = qty
        self.order_num = 0
        self.item_num = num

#init the obj array for the items
order_list = []
item_list = []
two_weeks = 7
holiday = [1, 45, 76, 104, 129, 171, 213, 214, 215, 216, 217, 218, 219, 
            220, 221, 222, 223, 224, 225, 226, 227, 228, 229 , 230, 304,
            331, 338, 345, 352, 353, 355, 356, 357, 360]
#this will pull the most current list from my git
url = "https://raw.githubusercontent.com/jgthornb/files/main/item_generation.txt"
page = requests.get(url)
local_file = 'item_copy.txt'
num_order = 0
xlsPos = 0
#saves a copy to the current folder. can be deleted later. 
with open(local_file, 'wb') as file:
    file.write(page.content)
#read the file and put the obj in to the array
fname = os.getcwd() + '\\' + local_file
def fill_list():
    with open(fname, "r") as myfile:
        for line in myfile:
            x = line.strip().split(", ")           
            item_list.append(item(x[0], int(x[1]), int(x[2]), int(x[3]), x[4], int(x[5])))
    for i in range(len(item_list)):        
        get_item_avg(item_list[i])        
        item_list[i].two_week_grace = item_list[i].store_avg * two_weeks

#prints out a specific object
def get_item_avg(self):
    self.store_avg = (random.randrange(self.min, self.max, 1))

def print_obj(self):
    print(self.name, self.min, self.max, self.dev, self.id, self.init_val)

def decrease_stock(self, item_use, day):  
    used =  math.ceil(item_use * self.weekend_mod)
    self.init_val -= used
    if self.init_val <= 0 and self.shipped == False:
        emergency_order(self)        
    if self.init_val < (self.store_avg * self.shipping_time) and self.shipped == False:       
        self.shipped = True 
        self.orders.append([day])                 

def need_ordering(self):
    if self.shipped == True:
        self.shipping_time -= 1       

def resupply_stock(self,day):
    if self.shipping_time == 0:
        self.init_val += self.two_week_grace
        self.shipping_time = 2
        self.shipped = False
        order_list.append(order(self.name,day, self.two_week_grace, self.id)) 

def weekend_check(self, day):
    day_check = day % 8
    if day_check >= 4:
        self.weekend_mod = (1 + ((day_check * 10)/100))
    elif day_check <= 1:
        self.weekend_mod = (1 - ((day_check * .5)/100)) 
    else:
        self.weekend_mod = 1

def emergency_order(self):    
    self.shipped = True
    self.init_val = 0
    self.shipping_time = 1

def the_loop(year):
    weather_input.execute(year)
    weather_cpy = copy.deepcopy(weather_input.weather_list) 
    for j in range(len(item_list)):
        holiday_incr = 0
        for i in range(365):
            #see if there is a holiday coming up, check for weather event. this is where we will make modifications to the avg
            mod_avg = item_list[j].store_avg * weather_cpy[i].weather_reduction
            if i == holiday[holiday_incr]:              
                mod_avg = mod_avg * item_list[j].holiday_mod               
                holiday_incr = (holiday_incr + 1) %  len(holiday)
            resupply_stock(item_list[j],i)
            weekend_check(item_list[j], i) 
            find_avg(item_list[j], i, mod_avg)           
            decrease_stock(item_list[j], mod_avg, i)
            need_ordering(item_list[j])          

#if folder does not exist, then it creates it 
def file_check(folder):
    check_folder = os.path.isdir(folder)
    if not check_folder:
        os.makedirs(folder)

def save_doc(folder):
    now = datetime.now()
    file_check(folder)
    f = open(os.getcwd() + "\\" + folder + "\data-gen-" + now.strftime("%H-%M-%S") +".txt", 'w+')
    for i in range(len(item_list)):
        f.write(str(item_list[i].name) + " " + str(item_list[i].orders) + "\n")
    f.close()
    
#what initiates all the work    
def execute():  
    global order_list         
    fill_list()
    the_loop(1)
    order_list.sort(key=lambda x:x.day)
    apply_order_num()
    #generate a filename that can be used in both xls and csv
    folder = timeDate()
    file = makeFileName(folder)
    xlsToCsv(save_xls(order_list, '2016',file,folder))
    order_list = []
    the_loop(2)
    order_list.sort(key=lambda x:x.day)
    apply_order_num()
    xlsToCsv(save_xls(order_list,'2017',file,folder))
    the_loop(3)
    order_list.sort(key=lambda x:x.day)
    apply_order_num()
    xlsToCsv(save_xls(order_list,'2018',file,folder))
    the_loop(4)
    order_list.sort(key=lambda x:x.day)
    apply_order_num()
    xlsToCsv(save_xls(order_list,'2019',file,folder))
    the_loop(5)
    order_list.sort(key=lambda x:x.day)
    apply_order_num()
    xlsToCsv(save_xls(order_list,'2020',file,folder))
    the_loop(6)
    order_list.sort(key=lambda x:x.day)
    apply_order_num()
    xlsToCsv(save_xls(order_list,'2021',file,folder))
    to_splitter = mergeXls(folder)   
    csvsplitter.seperate(to_splitter)
    #os.chdir("..\ML")
    os.chdir(BASE_DIR + "\ML")
    os.system("python MultiItemML.py")

def save_xls(self,year,file,folder):   
    global xlsPos
    file_check(folder)
    workbook = Workbook()    
    sheet = workbook.add_sheet('output',cell_overwrite_ok=False)
    sheet.write(0, 0, "Item")
    sheet.write(0, 1, "Item ID")
    sheet.write(0, 2, "Day")
    sheet.write(0, 3, "Quantity")
    sheet.write(0, 4, "Order Number")    
    for i in range(len(self)):
        sheet.write(i+1, 0, self[i].item_name)
        sheet.write(i+1, 1, self[i].item_num)
        sheet.write(i+1, 2, intToDate(self[i].day,year))
        sheet.write(i+1, 3, self[i].qty)
        sheet.write(i+1, 4, self[i].order_num)
    xlsPos = len(self)  
    #issue with the pi here. maybe
    workbook.save(file+"-"+year+".xls")
    return file+"-"+year

def timeDate():
    now = datetime.now()
    return now.strftime("%H-%M-%S-")

def mergeXls(folder):
    path = os.getcwd() +"\\" + folder
    xls_list = []
    for files in glob.glob(path+"\*.xls"):
        xls_list.append(pd.read_excel(files)) 
    merged = pd.concat(xls_list,ignore_index=True)
    mergedFile = folder +"\\"+"data_merged"
    merged.to_excel(mergedFile+".xls",index = False)
    xlsToCsv(mergedFile)
    return mergedFile

def makeFileName(folder):  
    return os.getcwd()+"\\"+folder+"\items-ordered-"+ timeDate()

def find_avg(self, day, use):
    if day < two_weeks:
        self.rolling_avg.append(use * self.weekend_mod)
    else:
        self.rolling_avg.append(use * self.weekend_mod)
        self.rolling_avg.pop(0) 
        avg = 0
        for i in range(len(self.rolling_avg)):
            avg += self.rolling_avg[i] 
        self.two_week_grace = math.ceil((avg/len(self.rolling_avg)) * two_weeks)

def order_day_print():
    for i in range(len(order_list)):
        print("item: "+ str(order_list[i].item_name) + " day: " + str(order_list[i].day) + " amount: "+ str(order_list[i].qty) + " order num: " + str(order_list[i].order_num))

def apply_order_num():    
    global num_order
    num_order += 1    
    for i in range(len(order_list)):
        if i == 0:
            order_list[i].order_num = num_order
        else:
            if order_list[i].day == order_list[i-1].day:
                order_list[i].order_num = num_order
            else:
                num_order += 1
                order_list[i].order_num = num_order

def intToDate(day,year): 
    day = str(day)
    day.rjust(3+len(day), '0')
    startDate = date(int(year),1,1)
    res_date = startDate + timedelta(days=int(day) - 1)
    return res_date.strftime("%m-%d-%Y")

def xlsToCsv(fileName):
    read_file = pd.read_excel(fileName+".xls")
    read_file.to_csv(fileName+".csv",index=None,header=True)
    return fileName
execute()