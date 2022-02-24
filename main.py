import requests
import configparser
import json

from flask import Flask, send_file
from flask_cors import CORS, cross_origin


# CREATE OBJECT
config_file = configparser.ConfigParser()
# READ CONFIG FILE
config_file.read("config.ini")
# Get the api_key
API_KEY = config_file['api']['api_key']


app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


def get_rijks(q):
    url = 'https://www.rijksmuseum.nl/api/nl/collection?key={}&imgonly=True&toppieces=True&q={}&s=relevance&ps=9'.format(
        API_KEY, q)
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()


def parse_rijks(data):
    """
    Function that will parse the rijksmuseam api response to filter out
    title, maker and imageurl
    """
    result = []
    for artObject in data['artObjects']:
        try:
            result.append({
                'id' : artObject['id'],
                'title': artObject['title'],
                'maker': artObject['principalOrFirstMaker'],
                'imageurl': artObject['webImage']['url']
            })
        except:
            pass
    return result


@app.route("/")
def index():
    """
    Using flask to serve static index.html.
    """
    return send_file('static/index.html')


@app.route("/favicon.ico")
def favicon():
    """
    Using flask to serve the facicon.
    """
    return send_file('static/favicon.ico')


@app.route('/get/<q>')
@cross_origin()
def get(q):
    data = get_rijks(q)
    result = parse_rijks(data)
    return {'result' : result}


if __name__ == "__main__":
    app.run(debug=True)
