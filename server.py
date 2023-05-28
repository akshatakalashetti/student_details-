from flask import Flask, request, jsonify
import csv

app = Flask(__name__)

# Load student details from a CSV file
def load_student_details():
    student_details = []

    with open('student_data.csv', 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            student_details.append(row)

    return student_details

# API endpoint for filtering student details
@app.route('/students/filter', methods=['POST'])
def filter_students():
    filters = request.json  # Assuming the UI sends filter criteria as JSON data

    student_details = load_student_details()

    filtered_data = []

    for student in student_details:
        # Apply filtering criteria to the student details
        if student['age'] >= filters.get('min_age', 0) and student['grade'] == filters.get('grade'):
            filtered_data.append(student)

    return jsonify(filtered_data)

if __name__ == '__main__':
    app.run()
