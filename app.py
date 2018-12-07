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
def KeyWord(text):
    KeyWordDict = {"嗨":"你這死賤畜",
                   "打":"你別再戳了好不好 去洗澡",
                   "豪":"說謊的人要吞一千斤精喔",
                   "來":"來什麼來 我就是要去妳妹的",
                   "玉米":"你這個母胎單身的魯蛇 老二比茄子還臭",
                   "嗨哥":"嗨哥在吞糞 別吵牠",
                   "肚臍":"守護家園 有你沒有我",
                   "加林":"都交女朋友了 什麼時候讓我們交流一下啊",
                   "育朕":"你的彩蛋太難想了 從缺",
                   "db":"別再找了 就是沒有你的",
                   "底逼":"放棄吧  你是被遺忘的",
                   "邢":"噓 別說那個人的名字 他會吃定你的蛋蛋的..",
                   "晚點":"每次說晚點都等到下禮拜了 你怎不晚點再尻槍",
                   "等等":"要多久 等你老婆懷上我的孩子嗎",
                   "==":"再吵我強姦你 讓你從嘴巴到屁眼都是我的洨",
                   ".":"說不出話來就去喝尿阿",
                   "哲":"嗨哥 我們也都是哲漢喔",
                   "芷":"宥軒 你是你鬥劍是鬥不過哲漢的 回去把綠帽戴好",
                   "累":"累啥 我把你操到中華民國萬萬歲喔",
                   "分鐘":"喔 是喔",
                   "有人":"這裡沒你的事 滾",
                   "滾":"好 我走 但是在我把你弄到懷孕後ㄎㄎ",
                   "快":"等你弄完換 我把你操的兵兵乓乓"}
    for k in KeyWordDict.keys():
        if text.find(KeyWord) != -1:
            return [True,KeyWordDict[KeyWord]]
    return [False]

def Reply(text):
    Ktemp = KeyWord(event.message.text)
    if Ktemp[0]:
        line_bot_api.reply_message(event.reply_token,
            TextSendMessage(text = Ktemp[1]))
    else:
        line_bot_api.reply_message(event.reply_token,
            TextSendMessage(text = event.message.text))

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
