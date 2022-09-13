from flask import Flask
from flask_cors import CORS
from datetime import datetime

from api import lostark

app = Flask(__name__)
CORS(app, resources={r'*': {'origins': 'http://lostarkapi.ga'}})


@app.route("/cmd/<string:args>")
def cmd(args):
    c = args.split(' ')
    print(c)
    if c[0] == "!명령어":
        return "!정보 | !부캐 | !장비 | !보석 | !악세 | !주간골드 | !스킬"
    elif c[0] == "!정보":
        return lostark.get_basic(c[1])
    elif c[0] == "!부캐":
        return lostark.get_sub_character(c[1])
    elif c[0] == "!장비":
        return lostark.get_equipment(c[1])
    elif c[0] == "!보석":
        return lostark.get_jewelry(c[1])
    elif c[0] == "!악세":
        return lostark.get_accessories(c[1])
    elif c[0] == "!주간골드":
        return lostark.get_week_gold(c[1])
    elif c[0] == "!스킬":
        return lostark.get_skill(c[1])
    elif c[0] == "퇴근시간":
        delta = datetime.strptime("19:00:00", "%H:%M:%S") - datetime.now()
        hour = delta.seconds / 3600
        minute = delta.seconds % 3600 / 60
        second = delta.seconds % 3600 % 60
        result = "퇴근까지 "
        if hour >= 0:
            result += f"""{hour}시 """

        if minute >= 0:
            result += f"""{minute}분 """

        if second >= 0:
            result += f"""{second}초 """

        result += "남았습니다."
        return ""
    else:
        return "알 수 없는 명령어 입니다."


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000', debug=True)
