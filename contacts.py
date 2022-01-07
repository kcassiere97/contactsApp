import mysql.connector
from flask import Flask
app = Flask(__name__)

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

    fn = "get fname"
    ln = "get lname"
    email = "get email"
    phone = "get number"
    #Create Database
    mycursor = db.cursor()
    mycursor.execute("CREATE DATABASE contactsDb")
    mycursor.execute("CREATE TABLE contact (fname VARCHAR(20), lname VARCHAR(20), phoneNumber VARCHAR(10), email VARCHAR(20))")
    mycursor.execute("INSERT INTO contactDb (fname,lname,phoneNumber,email) VALUES(?,?,?,?)",(fn,ln,email,phone))
    mycursor.commit()
    print("record added")
    db.close()
    
    return 'Success!'
    
if __name__ == '__main__':
   app.run(debug = True)

