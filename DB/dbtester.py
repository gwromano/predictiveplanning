import mysql.connector
from mysql.connector import Error


try:
    connection = mysql.connector.connect(host='167.224.250.163',
                                         database='Capstone',
                                         user='python-user',
                                         password='login_python_code',
                                         port = 3306)
    if connection.is_connected():
        query = 'Select * from item_testing'
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)
        cursor.execute(query)
        result = cursor.fetchall()
        print("\nPrinting the rows now")
        for row in result:
            print("Id= ",  row[0], )
            print("Price = " , row[1])
            print("Description = ", row[2])

except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
