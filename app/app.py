from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
app = Flask(__name__, static_folder='assets', static_url_path='/assets')
# Database configuration from environment variables
DATABASE_HOST = os.environ.get('DATABASE_HOST', 'localhost')
DATABASE_PORT = os.environ.get('DATABASE_PORT', 3306)
DATABASE_USER = os.environ.get('MYSQL_USER', 'flask_user')
DATABASE_PASSWORD = os.environ.get('MYSQL_PASSWORD', 'flask_password')
DATABASE_NAME = os.environ.get('MYSQL_DATABASE', 'flask_prod_db')

# Configure SQLAlchemy to use the MySQL database
app.config[
    'SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}'
app.config['SECRET_KEY'] = 'your_secret_key'  # for flash messages
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # To suppress a warning

db = SQLAlchemy(app)
