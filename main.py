from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage, PostbackEvent,TemplateSendMessage,ButtonsTemplate,MessageTemplateAction
import read
import sentence
import random

app = Flask(__name__)

# 這裡填入你的 Channel Access Token 和 Channel Secret
line_bot_api = LineBotApi('')
handler = WebhookHandler('')

all_word=[]
part_word=[]
read.read(all_word, part_word)
user_data={}
@app.route("/callback", methods=['POST'])
def callback():
    # 確認請求是來自LINE的
    signature = request.headers['X-Line-Signature']

    # 取得請求的body作為事件
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    user_id = event.source.user_id
    user_message = event.message.text.lower()

    # 初始化使用者資料
    if user_id not in user_data:
        user_data[user_id] = {
            'current_state': False,#判別是否開始測驗
            'question_list': [],#測驗題目
            'mistake_list':[],
            'this_mistake_list':[],
            'current':0,#當前題數
            'score':0,
            'user_answer':0,
            'current_answer':0,
            'current_question':[],
            'part':False,
            'token':100
        }

    # 取得使用者的狀態
    current_state = user_data[user_id]['current_state']

    user_message = event.message.text
    msgs=[]
    #判別rich menu
    if user_message.lower() == "start":
        user_data[user_id] = {
            'current_state': False,#判別是否開始測驗
            'question_list': [],#測驗題目
            'mistake_list':[],
            'this_mistake_list':[],
            'current':0,#當前題數
            'score':0,
            'user_answer':0,
            'current_answer':0,
            'current_question':[],
            'part':False,
            'token':100
        }
        
        if not user_data[user_id]['current_state']:
            reply_text = "開始測驗\n過程中點選End將結束測驗並輸出錯誤部分\n點選Start將初始化並從新開始"
            msgs.append(TextSendMessage(text=reply_text))
        else:
            reply_text = "從新測驗,先前紀錄初始化"
            msgs.append(TextSendMessage(text=reply_text))
        button_template_message = TemplateSendMessage(
            alt_text='Buttons template',
            template=ButtonsTemplate(
                title='測驗類型',
                text='請選擇測驗類型',
                actions=[
                    MessageTemplateAction(
                        label='全部單詞',
                        text='全部單詞',
                    ),
                    MessageTemplateAction(
                        label='a-z其中一個',
                        text='a-z其中一個',
                    ),
                ]
            )
        )
        msgs.append(button_template_message)
        user_data[user_id]['current_state']=True
    elif user_message.lower() == "keep":
        print(user_data[user_id]['current_state'])
        if not user_data[user_id]['current_state'] :#先前測驗結束
            print(1)
            reply_text = "新測驗"
            msgs.append(TextSendMessage(text=reply_text))
            user_data[user_id]['current_state']=True
            if len(user_data[user_id]['mistake_list'])<10:
                button_template_message = TemplateSendMessage(
                    alt_text='Buttons template',
                    template=ButtonsTemplate(
                        title='測驗類型',
                        text='請選擇測驗類型',
                        actions=[
                            MessageTemplateAction(
                                label='全部單詞',
                                text='全部單詞',
                            ),
                            MessageTemplateAction(
                                label='a-z其中一個',
                                text='a-z其中一個',
                            ),
                        ]
                    )
                )
                print(user_data[user_id])

            else:
                button_template_message = TemplateSendMessage(
                    alt_text='Buttons template',
                    template=ButtonsTemplate(
                        title='測驗類型',
                        text='請選擇測驗類型',
                        actions=[
                            MessageTemplateAction(
                                label='全部單詞',
                                text='全部單詞',
                            ),
                            MessageTemplateAction(
                                label='a-z其中一個',
                                text='a-z其中一個',
                            ),
                            MessageTemplateAction(
                                label='先前錯誤部分',
                                text='先前錯誤部分',
                            )
                        ]
                    )
                )
            msgs.append(button_template_message)
        else:#先前測驗尚未結束
            reply_text = "測驗尚未結束，請繼續測驗!\n結束請按end"
            msgs.append(TextSendMessage(text=reply_text))
            #test(user_data,user_id,msgs)
    elif user_message.lower() == "end":#測驗結束輸出錯誤部分
        reply_text = "結束測驗"
        msgs.append(TextSendMessage(text=reply_text))
        cout_end(user_data,user_id,msgs)#輸出錯誤內容
        user_data[user_id]['current_state'] = False#測驗結束
        user_data[user_id]['question_list'] = []#測驗題目
        user_data[user_id]['current']=0#當前題數
        user_data[user_id]['score']=0
        user_data[user_id]['user_answer']=0
        user_data[user_id]['current_answer']=0
        user_data[user_id]['current_question'] = []
        user_data[user_id]['part'] = False#測驗結束
        user_data[user_id]['token']=100
    #開始測驗判別是否選好內容
    elif user_data[user_id]['current_state'] and not user_data[user_id]['question_list']:
        if not user_data[user_id]['part']:#是否選part
            if len(user_data[user_id]['mistake_list'])<10:
                if user_message=='全部單詞':
                    user_data[user_id]['question_list']=all_word
                    test(user_data,user_id,msgs)
                elif user_message=='a-z其中一個':
                    user_data[user_id]['part']=True
                    reply_text = f"請輸入a-z其中一個"
                    msgs.append(TextSendMessage(text=reply_text))
                # else:
                #   reply_text = f"輸入錯誤,請輸入1或2"
                #   msgs.append(TextSendMessage(text=reply_text))
            else:
                if user_message=='全部單詞':
                    user_data[user_id]['question_list']=all_word
                    test(user_data,user_id,msgs)
                elif user_message=='a-z其中一個':
                    user_data[user_id]['part']=True
                    reply_text = f"請輸入a-z其中一個"
                    msgs.append(TextSendMessage(text=reply_text))
                elif user_message=='先前錯誤部分':
                    user_data[user_id]['question_list']=user_data[user_id]['mistake_list']
                    test(user_data,user_id,msgs)
                # else:
                #   reply_text = f"輸入錯誤,請輸入1,2或3"
                #   msgs.append(TextSendMessage(text=reply_text))
        else:
            num=ord(user_message.lower())-ord('a')
            if num>=0 and num<26:
                user_data[user_id]['question_list']=part_word[num]
                test(user_data,user_id,msgs)
            else:
                reply_text = f"輸入錯誤,請輸入a-z"
                msgs.append(TextSendMessage(text=reply_text))

    elif not user_data[user_id]['current_state']:#尚未點選
        reply_text = f"點選start可以開始測驗或點選end輸出結果"
        msgs.append(TextSendMessage(text=reply_text))
    elif user_data[user_id]['current_state'] and user_data[user_id]['question_list']:#開始測驗
        if user_message in ['1','2','3']:
            #判別前一題
            if user_message==user_data[user_id]['current_answer']:
                user_data[user_id]['score']+=10
            else:
                user_data[user_id]['mistake_list'].append(user_data[user_id]['current_question'])
                user_data[user_id]['this_mistake_list'].append(user_data[user_id]['current_question'])

            if user_data[user_id]['current']<10:
                test(user_data,user_id,msgs)
            else:
                msgs.append(TextSendMessage(text="測驗結束!"))
                msgs.append(TextSendMessage(text=f"Score: {user_data[user_id]['score']}"))
                cout(user_data,user_id,msgs)
                msgs.append(TextSendMessage(text="可從新點選Start,Keep或End\nStart:從新測驗,先前紀錄初始化\nKeep:繼續測驗\nEnd:將輸出錯誤部分"))
                user_data[user_id]['current_state'] = False#測驗結束
                user_data[user_id]['question_list'] = []#測驗題目
                user_data[user_id]['this_mistake_list']=[]
                user_data[user_id]['current']=0#當前題數
                user_data[user_id]['score']=0
                user_data[user_id]['user_answer']=0
                user_data[user_id]['current_answer']=0
                user_data[user_id]['current_question'] = []
                user_data[user_id]['part'] = False#測驗結束
                user_data[user_id]['token']=100
                #print(user_data)
        else:
            msgs.append(TextSendMessage(text="輸入錯誤，請重新輸入"))
    line_bot_api.reply_message(
        event.reply_token,
        msgs
    )

def test(user_data,user_id,msgs):
    word=user_data[user_id]['question_list']
    user_data[user_id]['current']+=1
    num1, num2, num3 = random.sample(range(len(word)), k=3)
    ans = random.randint(1, 3)
    user_data[user_id]['current_answer']=str(ans)
    
    if ans == 1:
        selected_num = num1
    elif ans == 2:
        selected_num = num2
    else:
        selected_num = num3
    user_data[user_id]['current_question']=word[selected_num]
    question=TextSendMessage(text=f"{str(user_data[user_id]['current'])}. {word[selected_num][1]}:\n(1) {word[num1][0]} (2) {word[num2][0]} (3) {word[num3][0]}")
    #u_ans_str=input(str(user_states[user_id]['current_question'])+'. '+word[selected_num][1]+':\n(1) '+word[num1][0]+'(2) '+word[num2][0]+'(3) '+word[num3][0]+'\n')
    msgs.append(question)
def cout_end(user_data,user_id,msgs):
    temp=user_data[user_id]['mistake_list']
    sentence.get_sentence(temp)
    temp_msgs='Mistake Words:\n'
    temp_msgs+='{:<20} {:<20} {:<40}\n'.format('單字', '意思','例句')
    #temp_msgs+='{:<15} {:<15}\n'.format('單字', '意思')
    for word in temp:
        if len(word)==2:
            temp_msgs += '{:<20} {:<20}\n'.format(word[0], word[1])
        else:
            temp_msgs+='{:<20} {:<20} {:<40}\n'.format(word[0], word[1],word[2])
    msgs.append(TextSendMessage(text=temp_msgs))

def cout(user_data,user_id,msgs):
    temp=user_data[user_id]['this_mistake_list']
    temp_msgs='Mistake Words:\n'
    temp_msgs+='{:<15} {:<15}\n'.format('單字', '意思')
    for word in temp:
        temp_msgs += '{:<15} {:<15}\n'.format(word[0], word[1])
    msgs.append(TextSendMessage(text=temp_msgs))

if __name__ == "__main__":
    app.run()
