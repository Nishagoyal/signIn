from flask import Flask, render_template, redirect, url_for, request,session
import pyodbc 
import pandas as pd
from werkzeug.security import generate_password_hash, check_password_hash

 
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello"

@app.route("/Login", methods=['GET', 'POST'])
def Login():
    error = None
    request_data=request.json
    print(request.json)
    #print(type(request.json))
    if request.method == 'POST':
        server = 'flask.database.windows.net' 
        database = 'flask12' 
        username = 'flask' 
        password = 'MkkI2785****'
        cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
        cursor = cnxn.cursor()
        
        
        cursor.execute(f"SELECT org_name, password FROM registration WHERE org_name ='{request_data['org_name']}'")
        user = cursor.fetchall()
        
        org_name= [lis[0] for lis in user]
        if len(org_name)==0:
            print ("list is empty")
        
        password= [lis[1] for lis in user]
        password2="".join(password)
        password1=request_data['password']
        
        # cursor.execute("select * from registration")
        # sql_query = pd.read_sql_query(f"SELECT * FROM registration1 ",cnxn)
        # print(sql_query)
        # print(type(sql_query))
       
        if (password1!=password2):
        
            print("hey")
            error = 'Invalid password'
            print(error)
        else:
            print("hey1")
            print('You were logged in')
            #session['email_id'] = email_id
       

        
        cnxn.close()
    return "done"

if __name__ == "__main__":
    
   app.run(host='0.0.0.0', port=5000)
    
