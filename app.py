
import requests
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World'
