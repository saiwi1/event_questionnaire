from discordwebhook import Discord

St_day = '5/6'
Su_day = '5/7'
We_day = '5/3'

data_01 = f'@DOPO\nオシリスの案内です。({St_day}・{Su_day})\n\n@DOPO\n<<通常オシリスの案内です>>\n\nお疲れ様です。\nさて、オシリスは4つのパターンにチームに分けします。\n金曜日の朝には登録しますので、木曜日に確認の上移動してください。\n希望の番号を押してください。'
data_02 = f':one: DOPO\n作戦あり / {St_day}土曜日22時\n\n:two: 71EX\n作戦あり / {St_day}土曜日22時\n\n:three: 71JC\n初動と基本役割だけあり / {St_day}土曜日22時\n\n:four: 713Q\n作戦あり / {Su_day}土曜日22時'
data_03 = f'締め切りは一応、{We_day}(水)UTC12:00までとします。\nそれ以降は空いているところにご案内させてもらいます。\n何か事情がある人は、事前にお知らせください。\nよろしくお願いします。'
data_to = data_01+'\n\n'+data_02+'\n\n'+data_03 
print(data_to)
with open('shiken.txt', mode='w',encoding = 'utf-8') as f:
     f.write(data_to)

discord = Discord(url="https://discord.com/api/webhooks/1025014985253982318/GjlWM_yhWFpnL3zhj-WZOSLTke3_e9QJRpgbGQZQvHRHw4j96USRhEKHgHwxE17GG0ZF")
discord.post(content=data_to)
