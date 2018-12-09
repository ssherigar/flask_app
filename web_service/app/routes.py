from app import app
import requests
import json

@app.route('/')
@app.route('/index')
def index():
    resp = requests.get('http://uinames.com/api/').content
    data = json.loads(resp)
    name = data['name']
    surname = data['surname']

    url = 'http://api.icndb.com/jokes/random?firstName=' + name + '&lastName=' + surname + '&limitTo=[nerdy]'

    resp = requests.get(url).content
    random_joke = json.loads(resp)
    joke = random_joke['value']['joke']
    return joke

