
import requests
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def index():
    url = 'http://api.openweathermap.org/data/2.5/weather?q=London,uk&APPID=9505be1fdbed303d342537db528a8c23'
    city = 'Dallas'

    r = requests.get(url.format(city)).json()
    print(r)


    return render_template('weather.html')


