# import module
import requests as rq
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

@handler.add( MessageEvent, message = TextMessage )
def handle_message( event ):

    attribute = event.message.text
    my_params = {"q": attribute}
    r = rq.get("http://drugtw.com/api/app", params = my_params)
    threshold = 10

    respond = ""

    for i in range( len( js.loads(r.text)["drug_table"] ) ):
        if i > threshold - 1:
            break
        respond += js.loads( r.text )["drug_table"][i]["chi_name"] + "\n"

    line_bot_api.push_message( event.source.user_id , 
                                TextSendMessage( text = respond ) )

    

if __name__ == "__main__":
    app.run()