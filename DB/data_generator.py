#The purpose of this program will be to create random data for our machine learning. 
import random
import requests
import os
from datetime import datetime

class item:
    def __init__(self, name, min, max, deviation, id):
        self.name = name
        self.min = min
        self.max = max
        self.dev = deviation
        self.orders = []
        self.id = id
#init the obj array for the items
item_list = []
#this will pull the most current list from my git
url = "https://raw.githubusercontent.com/jgthornb/files/main/item_generation.txt"
page = requests.get(url)
local_file = 'item_copy.txt'
#saves a copy to the current folder. can be deleted later. 
with open(local_file, 'wb') as file:
    file.write(page.content)
#read the file and put the obj in to the array
fname = os.getcwd() + '\\' + local_file
def fill_list():
    with open(fname, "r") as myfile:
        for line in myfile:
            x = line.strip().split(", ")           
            item_list.append(item(x[0], int(x[1]), int(x[2]), int(x[3]), x[4]))
#prints out a specific object
def print_obj(self):
    print(self.name, self.min, self.max, self.dev, self.id)

#begginning of the randomly generated data
def monthly_gen(self):
    i = 0
    while i < 12:
        self.orders.append(random.randrange(self.min, self.max, 1))
        i+=1

fill_list()
#testing with an item
for i in range(len(item_list)):
    monthly_gen(item_list[i])
    #i can probably move this into save_doc and save a loop

def save_doc():
    now = datetime.now()
    file_check()
    f = open(os.getcwd() + "\output\output"+ now.strftime("%H-%M-%S") +".txt", 'w+')
    f.write("{}{}{}{}{}{}{}{}{}{}{}{}{}\n".format(
        "Item"[0:15].ljust(15), "January"[0:10].ljust(10), "Febuary"[0:10].ljust(10),
        "March"[0:10].ljust(10),"April"[0:10].ljust(10), "May"[0:10].ljust(10), 
        "June"[0:10].ljust(10), "July"[0:10].ljust(10), "August"[0:10].ljust(10),
        "September"[0:10].ljust(10),"October"[0:10].ljust(10), "November"[0:10].ljust(10), 
        "December"[0:10].ljust(10)))
    #for i in item_list:
    for i in range(len(item_list)):
        f.write("{}{}{}{}{}{}{}{}{}{}{}{}{}\n".format(item_list[i].name[0:15].ljust(15), 
        str(item_list[i].orders[0])[0:10].ljust(10), str(item_list[i].orders[1])[0:10].ljust(10),
        str(item_list[i].orders[2])[0:10].ljust(10), str(item_list[i].orders[3])[0:10].ljust(10), str(item_list[i].orders[4])[0:10].ljust(10), 
        str(item_list[i].orders[5])[0:10].ljust(10), str(item_list[i].orders[6])[0:10].ljust(10), str(item_list[i].orders[7])[0:10].ljust(10),
        str(item_list[i].orders[8])[0:10].ljust(10), str(item_list[i].orders[9])[0:10].ljust(10), str(item_list[i].orders[10])[0:10].ljust(10), 
        str(item_list[i].orders[11])[0:10].ljust(10)))
    f.close()
def file_check():
    mydir = ("output")
    check_folder = os.path.isdir(mydir)
    if not check_folder:
        os.makedirs(mydir)

save_doc()
#print_obj(item_list[3])
# the next thing I want to work on is getting noise within the data that is generated. 
# this will involve using the same data and using random chance, (using the div value), to increase
# an order by a set amount. 
#*************
#side note: save_doc() can be condensed with another loop to clear up some lines. Not too pressing currently. 
#*************