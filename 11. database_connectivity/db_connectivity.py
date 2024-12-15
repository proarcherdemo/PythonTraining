import mysql.connector
from mysql.connector import Error


# Create a table in MySQL database 

import mysql.connector
from mysql.connector import Error


try: 
  
    # Step 1 - Get the connection object
    con = mysql.connector.connect(host='localhost', database='bankdb', user='root', password='root')
      
    # Step 2- From connection object get the cursor    
    cursor = con.cursor() 
      
    # Step -3 Execute the query using the cursor object
    cursor.execute("create database testdb")

    print("Database Created Successfully") 
                      
      
except Error as e: 
    print("Exception Raised while connecting - ", e) 
    #emailAPI
    #sms
    #slack/messaging api
  

finally: 
    if cursor: 
        cursor.close() 
    if con: 
        con.close() 
      

