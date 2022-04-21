import requests
import os
from datetime import datetime
import xlrd
import math


#this will pull the most current weather from my git
local_file = 'weather_copy.xls'
weather_list = []
thirty_avg = [] * 30
class weather:
    def __init__(self, temp, rain, snow):
        self.temp = temp
        self.rain = rain
        self.snow = snow 
        self.temp_avg = 0
        self.weather_reduction = 1
        

def get_data(year):
    if year == 6:
        dls = "https://github.com/jgthornb/files/raw/main/weather_data_capstone.xls"
    if year == 5:
        dls = "https://github.com/jgthornb/files/raw/main/2020_weather.xls"
    if year == 4:
        dls = "https://github.com/jgthornb/files/raw/main/2019_weather.xls"
    if year == 3:
        dls = "https://github.com/jgthornb/files/raw/main/2018_weather.xls"
    if year == 2:
        dls = "https://github.com/jgthornb/files/raw/main/2017_weather.xls"
    if year == 1:
        dls = "https://github.com/jgthornb/files/raw/main/2016_weather.xls"
    page = requests.get(dls)    
    #saves a copy to the current folder. can be deleted later. 
    #uncomment for mac
    #with open(os.getcwd() + "//output_weather//" + local_file, 'wb') as file:
    #uncommnet for windows
    with open(os.getcwd() + "//output_weather//" + local_file, 'wb') as file:
        file.write(page.content)

def file_check():
    mydir = ("output_weather")
    check_folder = os.path.isdir(mydir)
    if not check_folder:
        os.makedirs(mydir)

def read_file(year):
    global weather_list
    weather_list = []
    #uncomment for mac
    #loc = os.getcwd() + "//output_weather//" + local_file 
    #uncomment for windows
    loc = os.getcwd() + "//output_weather//" + local_file   
    wb = xlrd.open_workbook(loc)
    if year == 6:
        sheet = wb.sheet_by_name('all')
    if year == 5:
        sheet = wb.sheet_by_name('2020')
    if year == 4:
        sheet = wb.sheet_by_name('2019')
    if year == 3:
        sheet = wb.sheet_by_name('2018') 
    if year == 2:
        sheet = wb.sheet_by_name('2017')  
    if year == 1:
        sheet = wb.sheet_by_name('2016') 
    for i in range(sheet.nrows):  
            #print(sheet.cell_value(i,1),sheet.cell_value(i,2))
            avg_temp = str(sheet.cell_value(i,2))
            if i > 0:
                avg_temp = math.floor(float(avg_temp))
            else:
                avg_temp = 0
            rain = str(sheet.cell_value(i,3))
            snow = str(sheet.cell_value(i,4))
            weather_list.append(weather(avg_temp, rain, snow))
            thirty_day_avg(weather_list, i)
            
    weather_list.pop(0)
    populate_weather_mod()

def print_obj(self):
    print(self.temp, self.rain, self.snow, self.temp_avg)

def populate_weather_mod():
    for i in range(len(weather_list)): 
        weather_mod(weather_list, i)

def weather_mod(self, day):
    self[day].rain = float(self[day].rain) * 10
    if self[day].rain > 0:
        rain_log = math.log(self[day].rain, 10)
        rain_nlogn = self[day].rain * rain_log
    #After calculating the nlogn value, 
    #rain_nlogn will hold the % deficit value.
        rain_percent = rain_nlogn / 100
    else:
        rain_percent = 0
    if rain_percent > 0:
        rain_deficit = (1-rain_percent)
    else: 
        rain_deficit = 1
    self[day].weather_reduction = rain_deficit
    temp = self[day].temp
    snow  = float(self[day].snow)

    if temp < 32 and snow > 0.25:
        snow_deficit = 0.25
        self[day].weather_reduction = snow_deficit
    else:
        snow_deficit = 1
        self[day].weather_reduction = snow_deficit

# this will find the 30 day avg leading up to the day. 
# the purpose of which is to detect drastic changes in temp. 
def thirty_day_avg(self, day):
    avg_time = 30
    if day < avg_time:
        for i in range(day):
            self[day].temp_avg += self[i].temp
        self[day].temp_avg = self[day].temp_avg / (day+1)
    else:
        thirty_back = day - avg_time 
        while day > thirty_back:
            self[day].temp_avg += self[thirty_back].temp
            thirty_back += 1
        self[day].temp_avg = self[day].temp_avg / (avg_time + 1)

def execute(year):
    file_check()        
    get_data(year)
    read_file(year)

#execute()