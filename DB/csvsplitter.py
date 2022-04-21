#split one csv into individual item csv's
import pandas as pd
from tkinter.filedialog import askopenfilename
import os

#first checks for file on system
def file_check(folder):
    check_folder = os.path.isdir(folder)
    if not check_folder:
        os.makedirs(folder)
    return folder
#has the user select which file we are reading in. 
#this will be changed to a feeding in of data.
#fileDescriptor = askopenfilename()
#print(fileDescriptor)
def seperate(fileDescriptor):
    pos = os.getcwd()
    data = pd.read_csv(pos+"\\"+ fileDescriptor + ".csv",encoding = "ISO-8859-1")

    data_category_range = data['Item'].unique()
    data_category_range = data_category_range.tolist()
    folder = file_check("individual_csv")
    for i,value in enumerate(data_category_range):
        placement = pos+"\\"+folder+'\\Item_'+str(value)+'_.csv'
        #data[data['Item'] == value].to_csv(pos+folder+r'\Item_'+str(value)+r'.csv',index = False, na_rep = 'N/A')
        print(placement)
        data[data['Item'] == value].to_csv(placement,index = False, na_rep = 'N/A')
    get_files(pos+"\\"+folder)

def get_files(path):
    mylist = os.listdir(path)
    print(mylist)
