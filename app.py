import json as js
import requests as rq
from flask import Flask
app = Flask(__name__)

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

@app.route("/", methods = ["GET"])
def hello():
    return "Hi web!!"

@app.route("/callback", methods = ["POST"])
def callback():
    line_json = rq.get_json()
    return "line post!!"

if __name__ == "__main__":
    app.run()