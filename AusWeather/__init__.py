from flask import Flask

app = Flask(__name__)

from AusWeather import routes
