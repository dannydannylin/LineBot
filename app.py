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
handler = WebhookHandler("4339579df5c5d5b9451aba0af8434776")

@app.route("/", methods = ["GET"])
def hello():
    return "Hi web!!"

@app.route("/callback", methods = ["POST"])
def callback():
    
    json_line = request.get_json()
    print("I print something")
    return js.dumps( json_line )

@handler.add( MessageEvent, message = TextMessage )
def handle_message( event ):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage( text = "Yes Yes reply" ) )

if __name__ == "__main__":
    app.run()