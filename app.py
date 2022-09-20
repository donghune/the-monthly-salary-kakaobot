import random

from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r'*': {'origins': 'http://lostarkapi.ga'}})


@app.route("/cmd/<string:args>")
def cmd(args):
    if args[0] == "!":
        c = args.split(' ')
        if c[0] == "!명령어":
            return "!행사"
        elif c[0] == "!행사":
            return f"""
            2022년 한국관상어산업박람회
            2022.10.19 ~ 2022.10.23 
            http://www.kafaco.co.kr/pc/main/main.php
            """
        elif c[0] == '!가위바위보':
            bot_value = random.choice(['가위', '바위', '보'])
            if c[1] == "가위":
                if bot_value == "가위":
                    return "가위! 엥.. 무승부 다시해!"
                if bot_value == "바위":
                    return "바위! 아싸 내가 이겼다!"
                if bot_value == "보":
                    return "보! 뭐야.. 내가 졌잖아!"
            if c[1] == "바위":
                if bot_value == "바위":
                    return "바위! 엥.. 무승부 다시해!"
                if bot_value == "보":
                    return "보! 아싸 내가 이겼다!"
                if bot_value == "가위":
                    return "가위! 뭐야.. 내가 졌잖아!"
            if c[1] == "보":
                if bot_value == "보":
                    return "보! 엥.. 무승부 다시해!"
                if bot_value == "가위":
                    return "가위! 아싸 내가 이겼다!"
                if bot_value == "바위":
                    return "바위! 뭐야.. 내가 졌잖아!"
    else:
        if 'vs' in args:
            list = args.split('vs')
            return f"""당연히 {random.choice(list)}!"""
        elif '시베봇 넌 누가 만들었지?' == args:
            return "당연히 잘생긴 동훈님이죠!"
        elif "그치 시베봇?" == args:
            return f"""{random.choice(["인정!", "ㅇㅈㅇㅈ", "그치!", "맞아요!"])}"""


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000', debug=True)
