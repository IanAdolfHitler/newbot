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

# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message = TextSendMessage(text = Reply(event.message.text))
    line_bot_api.reply_message(event.reply_token, message)
def Reply(text):
    if text=="嗨":
        return "耖妳妹的畜牲"
    elif text=="打":
        return "我可以玩雷紋嗎"
    elif text=="來":
        return"你每次說來都還要1小時-.-"
    elif text=="晚點":
        return "晚點要多晚 再晚就要畢業啦"
    elif text=="有人要打嗎":
        return "並沒有 你是邊緣人"
    elif text=="@玉米":
        return "我可以玩雷紋嗎"

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
