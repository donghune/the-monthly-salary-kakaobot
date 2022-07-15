from flask import Flask
from flask_cors import CORS

from api import lostark

app = Flask(__name__)
CORS(app, resources={r'*': {'origins': 'http://152.70.248.4'}})


@app.route("/basic/<string:nickname>/")
def basic(nickname):
    return lostark.get_basic(nickname)


@app.route("/sub_character/<string:nickname>/")
def sub_character(nickname):
    return lostark.get_sub_character(nickname)


@app.route("/jewelry/<string:nickname>/")
def jewelry(nickname):
    return lostark.get_jewelry(nickname)


@app.route("/equipment/<string:nickname>/")
def equipment(nickname):
    return lostark.get_equipment(nickname)


@app.route("/accessories/<string:nickname>/")
def accessories(nickname):
    return lostark.get_accessories(nickname)


@app.route("/week_gold/<string:nickname>/")
def week_gold(nickname):
    return lostark.get_week_gold(nickname)


@app.route("/skill/<string:nickname>/")
def skill(nickname):
    return lostark.get_skill(nickname)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000', debug=True)
