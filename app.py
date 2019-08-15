
import requests
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import pprint

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///weather.db'

db = SQLAlchemy(app)

class City(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

@app.route('/')
def index():
    cities = City.query.all()

    weather_data = []

    for city in cities:

        url = 'http://api.openweathermap.org/data/2.5/weather?q=London,uk&APPID=9505be1fdbed303d342537db528a8c23'
        r = requests.get(url.format(city.name)).json()

        print(r)

        weather = {
            'name': city.name,
            'temperature': r['main']['temp'],
            'description': r['weather'][0]['description'],
            'icon': r['weather'][0]['icon']
        }

        weather_data.append(weather)

    # pprint.pprint(weather)
    return render_template('weather.html', weather_data=weather_data)


