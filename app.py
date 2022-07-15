from flask import Flask
from flask_cors import CORS

from api import lostark

app = Flask(__name__)
CORS(app, resources={r'*': {'origins': 'http://152.70.248.4'}})


@app.route("/")
def hello():
    return lostark.get_character_info_all("내월급돌려줘")["basic"]
