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

    # send opening words
    opening_words = "嗨，你好，請選擇您要查詢天氣或時間，"
    opening_words += "如果您要查詢天氣請打\"天氣\"，"
    opening_words += "如果您要查詢時間請打\"時間\"，"

    line_bot_api.push_message( event.source.user_id , 
                    TextSendMessage( text = opening_words ) )

    # input message ( choose which item do you want to inquire )
    msg = event.message.text

    if msg == "天氣":

        line_bot_api.push_message( event.source.user_id , 
                TextSendMessage( text = "您好，若想跳出天氣查詢請輸入\"滾\"" ) )

        while True:

            line_bot_api.push_message( event.source.user_id , 
                            TextSendMessage( text = "請輸入要查詢的城市(ex. 新北市)" ) )

            # input message ( choose which city do you want to inquire )
            msg = event.message.text

            if msg == "滾":
                break

            # weather info
            my_weather = weather.WeatherAPI()
            info = my_weather.getWeather( msg )

            line_bot_api.push_message( event.source.user_id , 
                                        TextSendMessage( text = info ) )

    elif msg == "時間":

        my_dateTime = dateTime.TimeAPI()
        info = my_dateTime.getTime()

if __name__ == "__main__":
    app.run()