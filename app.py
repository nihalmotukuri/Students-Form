from flask import Flask,  render_template, request, redirect
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient("mongodb+srv://nihalmotukuri:Ordt8X5eBJBMKZ4v@flask-cluster.eftmwx7.mongodb.net/?retryWrites=true&w=majority&appName=flask-cluster")
db = client["flask-db"]
collection = db["flask-col"]

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/students')
def get_students():
    students = list(collection.find())
    return render_template('students.html', students = students)

@app.route('/student', methods=['POST'])
def post_student():
    name = request.form['name']
    email = request.form['email']
    dob = request.form['date_of_birth']
    course = request.form['course']
    roll_number = request.form['roll_number']

    student_details = {
        "name": name,
        "email": email,
        "dob": dob,
        "course": course,
        "roll_number": roll_number}

    collection.insert_one(student_details)

    return redirect('/students')

if __name__ == "__main__":
    app.run(debug=True)