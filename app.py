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

def KeyWord(text):
	key={"豪":"豪妳妹","嗨":"想被打?"}
	for k in key.keys():
		if text.find(k) !=-1:
			return [True,key[k]]
	return [False]
def Button(event):
	message = TemplateSendMessage(
    	alt_text='Buttons template',
   		template=ButtonsTemplate(
       		thumbnail_image_url='https://example.com/image.jpg',
       		title='Menu',
       		text='Please select',
        	actions=[
            	PostbackTemplateAction(
               		label='postback',
               		text='postback text',
               		data='action=buy&itemid=1'
       		 	),
           		MessageTemplateAction(
            	   	label='message',
            	   	text='message text'
           		),
           		URITemplateAction(
                	label='uri',
               		uri='http://example.com/'
            	)
        	]
   		)
	)
line_bot_api.reply_message(event.reply_token, message)

def Reply(event):
	ktemp=KeyWord(event.message.text)
	if ktemp[0]:
		line_bot_api.reply_message(event.reply_token,TextMessage(text=ktemp[1]))
	else :
		line_bot_api.reply_message(event.reply_token,TextMessage(text=event.message.text))
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    try:
    	Button(event)
    	#Reply(event)
    except Exception as e:
    	line_bot_api.reply_message(event.reply_token,TextMessage(text=str(e)))
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
