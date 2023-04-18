from discordwebhook import Discord

St_day = '5/6'
Su_day = '5/7'
We_day = '5/3'

data_01 = f'@DOPO\n催事の案内です。({St_day}・{Su_day})\n\n@DOPO\n<<催事の案内です>>\n\nお疲れ様です。\nさて、今回のイベントは4つに分けします。\n金曜日の朝には振り分けします。\n希望の番号を押してください。'
data_02 = f':one: 設営担当\n 主に準備活動に従事、付属で呼び込み実施/ {St_day}土曜日9時に集合\n\n:two: 前半活動担当\n運営管理活動に従事 / {St_day}土曜日12時に集合\n\n:three: 後半活動担当\n運営管理活動に従事 / {Su_day}日曜日12時に集合\n\n:four: 撤収活動担当\n資材の回収及び清掃活動に従事 / {Su_day}日曜日15時に集合'
data_03 = f'締め切りは一応、{We_day}(水)12:00までとします。\nそれ以降は空いているところにご案内させてもらいます。\nなるべく連続して同じところを選択しないようにしてください。\nよろしくお願いします。'
data_to = data_01+'\n\n'+data_02+'\n\n'+data_03 
print(data_to)
with open('shiken.txt', mode='w',encoding = 'utf-8') as f:
     f.write(data_to)

discord = Discord(url="https://discord.com/api/webhooks/1025014985253982318/GjlWM_yhWFpnL3zhj-WZOSLTke3_e9QJRpgbGQZQvHRHw4j96USRhEKHgHwxE17GG0ZF")
discord.post(content=data_to)
