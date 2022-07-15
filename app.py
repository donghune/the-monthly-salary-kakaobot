from flask import Flask
from flask_cors import CORS

from api import lostark

app = Flask(__name__)
CORS(app, resources={r'*': {'origins': 'http://152.70.248.4'}})


@app.route("/basic/<string:nickname>/")
def basic(nickname):
    return lostark.get_character_info_all(nickname)["basic"] + " |  | " + \
           lostark.get_character_info_all(nickname)["level"] + " |  | " + \
           lostark.get_character_info_all(nickname)["stat"] + " |  | " + \
           lostark.get_character_info_all(nickname)["engrave"] + " |  | " + \
           lostark.get_character_info_all(nickname)["collections"]


@app.route("/sub_character/<string:nickname>/")
def sub_character(nickname):
    return lostark.get_character_info_all(nickname)["sub_character"]


@app.route("/jewelry/<string:nickname>/")
def jewelry(nickname):
    return lostark.get_character_info_all(nickname)["jewelry"]


@app.route("/equipment/<string:nickname>/")
def equipment(nickname):
    return lostark.get_character_info_all(nickname)["equipment"]


@app.route("/accessories/<string:nickname>/")
def accessories(nickname):
    return lostark.get_character_info_all(nickname)["accessories"] + " |  | " + \
           lostark.get_character_info_all(nickname)["ability_stone"]


@app.route("/week_gold/<string:nickname>/")
def week_gold(nickname):
    return lostark.get_character_info_all(nickname)["week_gold"]


@app.route("/skill/<string:nickname>/")
def skill(nickname):
    return lostark.get_character_info_all(nickname)["skill"]


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000', debug=True)
