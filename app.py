# import module
import json as js
import app
from flask import Flask, request, abort

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
    # get X-Line-Signature header value
    signature = request.headers["X-Line-Signature"]

    # get request body as text
    body = request.get_data( as_text = True )
    app.logger.info( "Request body: " + body )

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort( 400 )

    return "OK"

# @handler.add( MessageEvent, message = TextMessage )
# def handle_message( event ):
#     # line_bot_api.reply_message(
#     #     event.reply_token,
#     #     TextSendMessage( text = event.message.text ) )

#     line_bot_api.reply_message(
#         event.reply_token,
#         TextSendMessage( text = "Yes Yes Yes" ) )

@handler.add( MessageEvent )
def handle_message( event, destination ):
    print("do something")

if __name__ == "__main__":
    app.run()