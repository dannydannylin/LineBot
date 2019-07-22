# import module
import requests as rq
import json as js
from flask import Flask, request, abort

import weather
import dateTime

app = Flask( __name__ )

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

    msg = event.message.text

    if not( '天氣' in msg ) and ( msg != "時間" ):
        # send opening words
        opening_words = "嗨，您好，請選擇您要查詢天氣或時間，"
        opening_words += "如果您要查詢天氣請打\"XXX天氣\"(ex. 臺北市天氣)，"
        opening_words += "如果您要查詢時間請打\"時間\"。"

        line_bot_api.push_message( event.source.user_id , 
                        TextSendMessage( text = opening_words ) )

    elif '天氣' in msg:

        # weather info
        my_weather = weather.WeatherAPI()
        info = my_weather.getWeather( msg )

        line_bot_api.push_message( event.source.user_id , 
                                    TextSendMessage( text = info ) )

    elif msg == "時間":

        my_dateTime = dateTime.TimeAPI()
        info = my_dateTime.getTime()
        line_bot_api.push_message( event.source.user_id , 
                                    TextSendMessage( text = info ) )

if __name__ == "__main__":
    app.run()