'''
Lesson_5.py

           Steps to Connect to an SQLite3 Database 
1. Create a folder in the Root Directory and name it Database
2. Using the IDLE Integrated Development Environment (IDE) create a new Python file in the Database Directory and save it as lesson_5.py
3. Copy the below code and paste it into your lesson_5.py file then read the SQLite section of the Introduction to Python SQL Libraries article
4. Using the Terminal from the Database Directory, type python3 lesson_5,py to run the program
5. The Terminal will respond with,  Connection to SQLite DB successful
***************************************************************************************
'''

import sqlite3
from sqlite3 import Error

def create_connection(pathToDataBase):
    connection = None
    try:
        connection = sqlite3.connect(pathToDataBase)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection   

connection = create_connection("toDatabase")
