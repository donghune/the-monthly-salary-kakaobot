from flask import Flask
from flask_cors import CORS

from api import lostark

app = Flask(__name__)
CORS(app, resources={r'*': {'origins': 'http://152.70.248.4'}})


@app.route("/basic/<string:nickname>/")
def basic(nickname):
    return lostark.get_character_info_all(nickname)["basic"]


@app.route("/level/<string:nickname>/")
def level(nickname):
    return lostark.get_character_info_all(nickname)["level"]


@app.route("/sub_character/<string:nickname>/")
def sub_character(nickname):
    return lostark.get_character_info_all(nickname)["sub_character"]


@app.route("/stat/<string:nickname>/")
def stat(nickname):
    return lostark.get_character_info_all(nickname)["stat"]


@app.route("/engrave/<string:nickname>/")
def engrave(nickname):
    return lostark.get_character_info_all(nickname)["engrave"]


@app.route("/ability_stone/<string:nickname>/")
def ability_stone(nickname):
    return lostark.get_character_info_all(nickname)["ability_stone"]


@app.route("/jewelry/<string:nickname>/")
def jewelry(nickname):
    return lostark.get_character_info_all(nickname)["jewelry"]


@app.route("/equipment/<string:nickname>/")
def equipment(nickname):
    return lostark.get_character_info_all(nickname)["equipment"]


@app.route("/week_gold/<string:nickname>/")
def week_gold(nickname):
    return lostark.get_character_info_all(nickname)["week_gold"]


@app.route("/accessories/<string:nickname>/")
def accessories(nickname):
    return lostark.get_character_info_all(nickname)["accessories"]


@app.route("/skill/<string:nickname>/")
def skill(nickname):
    return lostark.get_character_info_all(nickname)["skill"]


@app.route("/collections/<string:nickname>/")
def collections(nickname):
    return lostark.get_character_info_all(nickname)["collections"]


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000', debug=True)
