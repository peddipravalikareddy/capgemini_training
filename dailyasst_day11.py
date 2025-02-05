# Create a table in MySQL with min 7 columns 
# Perform crud operations on it
# Filter the details on the basis of gender 
# Filter the details on basis of department

from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app)

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Pravalika31",
    database="student"
)

cursor = conn.cursor()

cursor.execute("use student")

# Get all students
@app.route('/users', methods=['GET'])
def get_students():
    cursor.execute("SELECT * FROM students")
    users = cursor.fetchall()
    return jsonify(users)

# Get student using roll number
@app.route('/users/<roll>', methods=['GET'])
def get_student(roll):
    cursor.execute("SELECT * FROM students where rollNo=%s", (roll,))
    user = cursor.fetchone()
    if user:
        return jsonify(user)
    return jsonify({"message": "User not found"}), 404

# Get users by gender
@app.route('/users/gender=<gender>', methods=['GET'])
def get_students_by_gender(gender):
    cursor.execute("SELECT * FROM students WHERE lower(gender)=lower(%s)", (gender,))
    users = cursor.fetchall()
    if users:
        return jsonify(users)
    return jsonify({"message": "No users found"}), 404

# Get department wise students
@app.route("/users/dept=<dept>", methods=['GET'])
def get_students_by_dept(dept):
    cursor.execute("select * from students where dept=lower(%s)", (dept,))
    users = cursor.fetchall()
    if users:
        return jsonify(users)
    return jsonify({"message": "No users found"}), 404


# Add student
@app.route('/users', methods=['POST'])
def add_student():
    data = request.json
    name = data['name']
    roll = data['rollNo']
    email = data['email']
    dept = data['dept']
    gender = data['gender']
    favSub = data['favSub']
    gpa = data['gpa']
    cursor.execute("INSERT INTO students VALUES (%s, %s, %s, %s, %s, %s, %s)", (name, roll, email, dept, gender, favSub, gpa))
    conn.commit()
    return jsonify({"message": "User added successfully"}), 201

# Update student details
@app.route('/users/<roll>', methods=['PUT'])
def update_student(roll):
    data = request.json
    name = data['name']
    email = data['email']
    dept = data['dept']
    gender = data['gender']
    favSub = data['favSub']
    gpa = data['gpa']
    cursor.execute("UPDATE students SET name=%s, email=%s, dept=%s, gender=%s, favSub=%s, gpa=%s WHERE rollNo=%s", (name, email, dept, gender, favSub, gpa, roll))
    conn.commit()
    return jsonify({"message": "User updated successfully"})

# Delete a student

@app.route('/users/<roll>', methods=['DELETE'])
def delete_student(roll):
    cursor.execute("DELETE FROM students WHERE rollNo=%s", (roll,))
    conn.commit()
    return jsonify({"message": "User deleted successfully"})

# Get total count of users
@app.route("/users/total", methods=["GET"])
def get_total_student_count():
    cursor.execute("select count(*) from students")
    count = cursor.fetchall()
    return jsonify(count)

if __name__ == "__main__":
    app.run(debug=True)