# 
# Authors: Justin Sandstedt, Matthew Swandal, Gabriel Morgan
# Flask framework to allow HTML input into SQL tables to store information securely. 
# Must run " pip install flask flask-mysql flask-bcrypt " in terminal
#
#
#

from flask import Flask, render_template, request, redirect
import mysql.connector
from flask_bcrypt import Bcrypt

app = Flask(__name__)
bcrypt = Bcrypt(app)

# Connect to MySQL
db = mysql.connector.connect(
    host="localhost", #
    user="", # Identify username 
    password="", # created pw from SQL connection?
    database="" #my db name?
)
cursor = db.cursor()

# Route to render the signup page.
@app.route('/')
def signup_page():
    return render_template('signup.html')

# Route to handle form submission with query to insert SQL fields. 
@app.route('/register', methods=['POST'])
def register():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    password = bcrypt.generate_password_hash(request.form['password']).decode('utf-8')  # Hash password
    date_of_birth = request.form['date_of_birth']
    gender = request.form['gender']
    activity_level = request.form['activity_level']

    query = "INSERT INTO users (first_name, last_name, email, password_hash, date_of_birth, gender, activity_level) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    values = (first_name, last_name, email, password, date_of_birth, gender, activity_level)
    
    cursor.execute(query, values)
    db.commit()
    
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
