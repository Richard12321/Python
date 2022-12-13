from flask import *
from flask_restful import Api, Resource
from RPSSL import play

class statistics(Resource):
    def get(self):
        with open('RPSSL/RPSSL.json', 'r') as file:
            return json.load(file)

app = Flask(__name__)
api = Api(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/game')
def game():
    return render_template('game.html', test='test')

@app.route('/pick/<string:pick>/<int:mode>')
def pick(pick, mode): 
    res = play(pick, mode) 
    return render_template('game.html', result=res)

api.add_resource(statistics, '/stats')

app.run(debug=True)

