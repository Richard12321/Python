from flask import *
from flask_restful import Api, Resource
from RPSSL import play

class statistics(Resource):
    def get(self):
        with open('RPSSL/RPSSL.json', 'r') as file:
            return json.load(file)

app = Flask(__name__)
api = Api(app)

app.secret_key = '48c1cb4d1388f1504ce904f8b875da9f51f0466d322d3120ec32b0ee14ba40f9'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/game')
def game():
    return render_template('game.html', test='test')

@app.route('/pick/<string:pick>/<int:mode>/<string:name>')
def pick(pick, mode, name):
    if 'lastPick' not in session: 
        session['lastPick'] = ''
    res = play(pick, mode, session['lastPick'], name)
    session['lastPick'] = pick

    return render_template('game.html', result=res)

api.add_resource(statistics, '/stats')

app.run(debug=True)
