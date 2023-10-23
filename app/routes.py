from app import app
from flask import render_template


@app.route('/')
def index():
    return render_template('main.html')


@app.route('/about')
def about():
    return "This is the about page."


@app.route('/consultations')
def consultations():
    return "View available consultations here."


@app.route('/reserve/<int:consultation_id>')
def reserve(consultation_id):
    return f"Reserve consultation with ID {consultation_id}."

# You can add more routes as needed
