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
    else:
        if 'vs' in args:
            list = args.split('vs')
            return f"""당연히 {random.choice(list)}!"""


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000', debug=True)
