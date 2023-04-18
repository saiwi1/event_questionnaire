import PySimpleGUI as sg                                 
from discordwebhook import Discord
import datetime

dt_now = datetime.datetime.now()
dt_win = dt_now.strftime('%Y年%m月%d日')
dt_Pl7 = dt_now+datetime.timedelta(days=7)
dt_set_day = dt_Pl7.strftime('%Y/%m/%d')

# ウィンドウの内容を定義する
layout = [  [sg.Text("次の催事の開催の土曜日は何日？")],     
            [sg.Input(default_text = dt_set_day,key='-DATE-')],
            [sg.Text(size=(55,1), key='-OUTPUT-')],
            [sg.Button('この日だ！'),sg.Button('終了')]] 
# ウィンドウを作成する
window = sg.Window(f'催事開催案内の準備（今日は{dt_win}です。）', layout)      
while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED or event == '終了':
        break
    window['-OUTPUT-'].update( values['-DATE-']+ "この日から動く計画")

    str_day = values['-DATE-']
  
    dte = datetime.datetime.strptime(str_day, '%Y/%m/%d')
    dt_Pl1 = dte+datetime.timedelta(days=+1)
    dt_Mi3 = dte+datetime.timedelta(days=-3)

    
    St_day = dte.strftime('%m月%d日')
    Su_day = dt_Pl1.strftime('%m月%d日')
    We_day = dt_Mi3.strftime('%m月%d日')
    
    data_01 = f'@DOPO\n催事の案内です。({St_day}・{Su_day})\n\n@DOPO\n<<催事の案内です>>\n\nお疲れ様です。\nさて、今回のイベントは4つに分けします。\n金曜日の朝には振り分けします。\n希望の番号を押してください。'
    data_02 = f':one: 設営担当\n 主に準備活動に従事、付属で呼び込み実施/ {St_day}土曜日9時に集合\n\n:two: 前半活動担当\n運営管理活動に従事 / {St_day}土曜日12時に集合\n\n:three: 後半活動担当\n運営管理活動に従事 / {Su_day}日曜日12時に集合\n\n:four: 撤収活動担当\n資材の回収及び清掃活動に従事 / {Su_day}日曜日15時に集合'
    data_03 = f'締め切りは一応、{We_day}(水)12:00までとします。\nそれ以降は空いているところにご案内させてもらいます。\nなるべく連続して同じところを選択しないようにしてください。\nよろしくお願いします。'
    data_to = data_01+'\n\n'+data_02+'\n\n'+data_03 
    print(data_to)
    with open('shiken.txt', mode='w',encoding = 'utf-8') as f:
        f.write(data_to)

    discord = Discord(url="dwebhookアドレス")
    discord.post(content=data_to)



# 画面から削除して終了
window.close() 