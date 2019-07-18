import json as js

from flask import Flask, request
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

line_bot_api = LineBotApi("6S5y3NrPtinBzdKDiArf/AoCyJwpimZtov/uQbod/1gTtZGU+Kaapc23A5DYIpRosCBfBKk+YdqqNOXi5EmnqaqCmG4CetaCfdnkxH0QE2lKy0ulvGwF0geDSUV9qfYW1ioFU49EEbxFpzdgKGHBBQdB04t89/1O/w1cDnyilFU=")
handler = WebhookHandler('YOUR_CHANNEL_SECRET')

@app.route("/", methods = ["GET"])
def hello():
    return "Hi web!!"

@app.route("/callback", methods = ["POST"])
def callback():
    print("I print something")
    # line_json = request.get_data()
    return "callback"

if __name__ == "__main__":
    app.run()