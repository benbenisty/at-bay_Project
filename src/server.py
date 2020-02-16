
from flask import Flask, render_template, json, request, redirect
import mysql.connector

#connect to the Database
app = Flask(__name__)

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="new_password",
    database="db1"
)

mycursor = mydb.cursor()

#main-page
@app.route('/', methods=['POST', 'GET'])
def main():
        mycursor.execute("SELECT * FROM employees")
        fetchall = mycursor.fetchall()

        return render_template('index.html', data = fetchall)

#add-page
@app.route('/add', methods=['POST', 'GET'])
def add():

    if request.method == 'POST':
        sql = """INSERT INTO employees
                    VALUES (5,'rty', 'rfdc', 'bxd', 'fdcdx')"""
        mycursor.execute(sql)
        mydb.commit()

    return render_template('add.html')

#edit-page
@app.route('/edit', methods=['POST', 'GET'])
def edit():
    if request.method == 'POST':
         sql = "UPDATE employees SET first_name = %s WHERE last_name = %s"
         val = ("eerff", "eee")
         mycursor.execute(sql,val)
         mydb.commit()
    return render_template('edit.html')

#run the app
if __name__ == '__main__':
	app.run()