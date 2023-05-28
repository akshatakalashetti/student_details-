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

# API endpoint for retrieving paginated student details
@app.route('/students', methods=['GET'])
def get_paginated_students():
    page = request.args.get('page', default=1, type=int)
    page_size = request.args.get('page_size', default=10, type=int)

    student_details = load_student_details()

    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    paginated_data = student_details[start_index:end_index]

    return jsonify(paginated_data)

if __name__ == '__main__':
    app.run()
