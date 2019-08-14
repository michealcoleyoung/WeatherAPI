
import requests
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import pprint

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def index():
    url = 'http://api.openweathermap.org/data/2.5/weather?q=London,uk&APPID=9505be1fdbed303d342537db528a8c23'
    city = 'Dallas'

    r = requests.get(url.format(city)).json()
    pprint.pprint(r)

    weather = {
        'name': city,
        'temperature': r['main']['temp'],
        'description': r['weather'][0]['description'],
        'icon': r['weather'][0]['icon']
    }

    pprint.pprint(weather)
    return render_template('weather.html', weather=weather)


