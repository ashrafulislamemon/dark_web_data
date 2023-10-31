
import mysql.connector
import re
import random 


arr=['a','b','c']

conn = mysql.connector.connect(user='root', password='', host='localhost', database='test_database_ashraf')
cursor = conn.cursor()

sql = "SELECT data FROM data_table WHERE data = 'b';"
cursor.execute(sql)
data = cursor.fetchall()

cursor.close()
conn.close()
print(data)
if len(data)>0:


    for i in arr:
       
        conn = mysql.connector.connect(user='root', password='', host='localhost', database='test_database_ashraf')
        cursor = conn.cursor()
        new_value = i     
        sql = "UPDATE data_table SET name = CONCAT(name, %s) WHERE data = 'b';"       
        cursor.execute(sql, (', ' + new_value,))      
        conn.commit()

        cursor.close()
        conn.close()




