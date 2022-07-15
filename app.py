from flask import Flask
from flask_cors import CORS

from api import lostark

app = Flask(__name__)
CORS(app, resources={r'*': {'origins': 'http://152.70.248.4'}})


@app.route("/cmd/<string:args>")
def cmd(args):
    if args == "!명령어":
        return "!정보 | !부캐 | !장비 | !보석 | !악세 | !주간골드 | !스킬"
    elif args[0] == "!정보":
        return lostark.get_basic(args[1])
    elif args[0] == "!부캐":
        return lostark.get_sub_character(args[1])
    elif args[0] == "!장비":
        return lostark.get_jewelry(args[1])
    elif args[0] == "!보석":
        return lostark.get_equipment(args[1])
    elif args[0] == "!악세":
        return lostark.get_accessories(args[1])
    elif args[0] == "!주간골드":
        return lostark.get_week_gold(args[1])
    elif args[0] == "!스킬":
        return lostark.get_skill(args[1])
    else:
        return "알 수 없는 명령어 입니다."


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000', debug=True)
