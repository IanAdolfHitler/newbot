from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi('1WUu6duAA0P7ofV4J3earPdrX8masnaN6hdy6cTctFZJxTG1eWrE51wfbM6wBZtxFRU6qR2+J9+GGAxlIfWl5ZFi6blqDaLV6Pedy3YI8RDpMQjyhlkzQI1pDWwwsOgXGNSbLmpS4qwM96rSNYBFtwdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('0963231f909332b42026ae9515df6757')

# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'
#關鍵字系統
def Keyword(event):
    KeyWordDict = {"你好":["text","你也好啊"],
                   "你是誰":["text","我是大帥哥"],
                   "差不多了":["text","讚!!!"],
                   "帥":["sticker",'1','120']}

    for k in KeyWordDict.keys():
        if event.message.text.find(k) != -1:
            if KeyWordDict[k][0] == "text":
                line_bot_api.reply_message(event.reply_token,TextSendMessage(text = KeyWordDict[k][1]))
            elif KeyWordDict[k][0] == "sticker":
                line_bot_api.reply_message(event.reply_token,StickerSendMessage(
                    package_id=KeyWordDict[k][1],
                    sticker_id=KeyWordDict[k][2]))
            return True
    return False

#按鈕版面系統
def Button(event):
    line_bot_api.reply_message(event.reply_token,
        TemplateSendMessage(
            alt_text='特殊訊息，請進入手機查看',
            template=ButtonsTemplate(
                thumbnail_image_url='https://github.com/54bp6cl6/LineBotClass/blob/master/logo.jpg?raw=true',
                title='HPClub - Line Bot 教學',
                text='大家學會了ㄇ',
                actions=[
                    PostbackTemplateAction(
                        label='還沒',
                        data='還沒'
                    ),
                    MessageTemplateAction(
                        label='差不多了',
                        text='差不多了'
                    ),
                    URITemplateAction(
                        label='幫我們按個讚',
                        uri='https://www.facebook.com/ShuHPclub'
                    )
                ]
            )
        )
    )

#指令系統，若觸發指令會回傳True
def Command(event):
    tempText = event.message.text.split(",")
    if tempText[0] == "發送" and event.source.user_id == "Uad9ac35b0ebba03da9c51ab1516a18ca":
        line_bot_api.push_message(tempText[1], TextSendMessage(text=tempText[2]))
        return True
    else:
        return False

#回覆函式，指令 > 關鍵字 > 按鈕
def Reply(event):
    if not Command(event):
        if not Keyword(event):
            Button(event)

# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    try:
        Reply(event)
        '''
        line_bot_api.push_message("Uad9ac35b0ebba03da9c51ab1516a18ca", TextSendMessage(text=event.source.user_id + "說:"))
        line_bot_api.push_message("Uad9ac35b0ebba03da9c51ab1516a18ca", TextSendMessage(text=event.message.text))
        '''
    except Exception as e:
        line_bot_api.reply_message(event.reply_token, 
            TextSendMessage(text=str(e)))

#處理Postback
@handler.add(PostbackEvent)
def handle_postback(event):
    command = event.postback.data.split(',')
    if command[0] == "還沒":
        line_bot_api.reply_message(event.reply_token, 
            TextSendMessage(text="還沒就趕快練習去~~~"))
        
@handler.add(MessageEvent, message=StickerMessage)
def handle_sticker_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        StickerSendMessage(
            package_id='1',
            sticker_id='410')
    )

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
