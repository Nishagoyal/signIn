from flask import Flask, render_template, redirect, url_for, request,session
import pyodbc 
import pandas as pd
from werkzeug.security import generate_password_hash, check_password_hash
from flask_bcrypt import Bcrypt
app = Flask(__name__)
bcrypt = Bcrypt(app)
@app.route("/")
def home():
    return "Hello"

@app.route("/ngo_order", methods=['GET', 'POST'])
def SignIn():
    try:
        error = None
        request_data=request.json
        print(request.json)
        #print(type(request.json))
        if request.method == 'POST':
            server = 'flask.database.windows.net' 
            database = 'flask12' 
            username = 'flask' 
            password = //write password
            cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
            cursor = cnxn.cursor()
            
            cursor.execute(f"INSERT INTO OrderTable VALUES ('{request_data['ngo_name']}','{request_data['org_name']}','{request_data['food_name']}','{request_data['quantity']}')")
            
            cnxn.commit()
            return "done"
    finally:
        
        cursor.close()
        cnxn.close()
       
   

        
if __name__ == "__main__":
    
   app.run(host='0.0.0.0', port=5000)
    


