import mysql.connector
conn = mysql.connector.connect(host='127.0.0.1',username= 'root',password= '12345678',database="test3")
if conn.is_connected():
    print("Connection established...")
    cursor=conn.cursor()
    select_query="SELECT * from test_table where id=1"
    cursor.execute(select_query)
    rows=cursor.fetchall()
    for row in rows:
        print(row)    

import mysql.connector 
conn=mysql.connector.connect(host= '127.o.o.1',username='root',password= '12345678',database= "test3")
if conn.is_connected() :
    print("Connection established...")
    cursor=conn.cursor ()
    select_query = "select * from test_table where id=1"
    cursor.execute(select_query)
    rows=cursor.fetchall()
    for row in rows :
        print(row)

import mysql.connector
conn=mysql.connector.connect(host='127.0.0.1',username= 'root', password= '12345678',database= "test3")
if conn.is_connected() :
    print("Connection established...")
    cursor=conn.cursor () 
    select_query = "SELECT * from test_table where id=1"
    cursor.execute(select_query)
    rows=cursor.fetchall()
    for row in rows :
        print(row)