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
        return "請支付100元以繼續使用!"
    elif text=="打":
        return "打妳妹 打我手槍"
    elif text=="來打":
        return "又想送頭 真的是送的不知不覺ㄟ"
    elif text=="來":
        return"你每次說來都還要1小時-.-"
    elif text=="晚點":
        return "晚點要多晚 再晚就要畢業啦"
    elif text=="有人要打嗎":
        return "並沒有 你是邊緣人"
    elif text=="@玉米":
        return "你個龜孫子"
    elif text=="玉米":
        return "就一個單身19年的魯蛇 懶趴比茄子還紫"
    elif text=="豪":
        return "說謊的人 要吞一千斤精喔"
    elif text=="聰明的機器人阿 你覺得葡萄如何":
        return "爛透了 跟沒洗過的包皮垢一樣臭"
    elif text=="@葡萄":
        return "葡萄在跟我摔角"
    elif text=="哲漢":
        return "嗨歌你還想要嗎?"
    elif text=="嗨哥":
        return "嗨哥在挖糞 別吵他"
    elif text=="閉嘴":
        return "我用老二撬開你嘴巴喔"
    elif text=="嗎":
        return "可以好好打字嗎 你乙武洋匡?"
    elif text=="==":
        return "再吵我槍斃你"
    elif text=="你有什麼願望呢":
        return "客家人同性戀三餐都吃核廢料 通通關進毒氣室"
    elif text=="加林":
        return "嫂子真棒"
    elif text=="肚臍":
        return "你愛護家園 家園守護你"
    elif text=="db":
        return "育朕你什麼時候升大學"
    elif text=="嫂子":
        return "加林比較弱 你就將就一下吧"
    elif text=="芷君":
        return "哲漢你好厲害 你看宥軒都抬不起來"

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
