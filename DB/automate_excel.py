import mysql.connector
from mysql.connector import Error
import xlrd
import xlwt
import os
import pandas.io.sql as sql
from configparser import ConfigParser

loc = r'd:\Programs\documentation\DB\uniqueUPC_for_test_db.xls'
print(loc)
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
try:
    connection = mysql.connector.connect(host='167.224.250.163',
                                         database='Capstone',
                                         user='python-user',
                                         password='login_python_code',
                                         port = 3306)
    if connection.is_connected():
        for i in range(sheet.nrows):  
            print(sheet.cell_value(i,0),sheet.cell_value(i,1))
            t_id = str(sheet.cell_value(i,0))
            t_price = str(sheet.cell_value(i,1))
            t_descp = str(sheet.cell_value(i,2))
            query = "INSERT INTO item_testing (id, price, description) VALUES ("+t_id+", "+t_price+", '"+t_descp+"')"
            print(query)
            cursor = connection.cursor()
            cursor.execute(query)
            connection.commit()
            print(cursor.rowcount, "Record inserted successfully into pi table")
        
       
except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
