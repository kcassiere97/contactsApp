import mysql.connector
import Flask as flask



app = flask(__name__)

@app.route('/')
def contacts():

    #Initialize Database 
    db = mysql.connector.connect(
        host = "localhost",
        username = "user",
        password = "pass"
    )

    if mysql.connector.Error:
        print("Failed to connect to database")
    else:
        print("Connected Successfully")

    #Create Database
    mycursor = db.cursor()
    mycursor.execute("CREATE DATABASE contactsDb")
    mycursor.execute("CREATE TABLE contact (fname VARCHAR(20), lname VARCHAR(20), phoneNumber VARCHAR(10), email VARCHAR(20))")
    db.close()
    
    return 'Success!'
    


