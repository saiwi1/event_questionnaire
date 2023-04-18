import PySimpleGUI as sg 
import os
import win32com.client
import datetime
import openpyxl

# ウィンドウの内容を定義する
layout = [  [sg.Text("次の催事の開催の土曜日は何日？")],     
            [sg.Input(key='-DATE-')],
            [sg.Text(size=(55,1), key='-OUTPUT-')],
            [sg.Button('この日だ！'),sg.Button('終了')]] 
# ウィンドウを作成する
window = sg.Window('催事案内の準備', layout)      
while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED or event == '終了':
        break
    window['-OUTPUT-'].update( values['-DATE-']+ "この日を基準に作成するね")
    dt_now = datetime.datetime.now()
    str_dt_today = dt_now.strftime('%Y_%m_%d%H%M')
    file_name= str_dt_today+'AooInfo.xlsx'


    wb=openpyxl.load_workbook('Aooinformation.xlsx')
    ws = wb.active
    ws['B3'] = values['-DATE-']

    wb.save(file_name)
    wb.close()

    dir_now =os.getcwd()+'/'

    excel = win32com.client.Dispatch("Excel.Application")
    filename= dir_now+file_name
    filename_pro = filename[:-5]
    filename_in = filename_pro + '.pdf'
    wb = excel.Workbooks.Open(filename)
    wb.WorkSheets(1).Select()
    wb.ActiveSheet.ExportAsFixedFormat(0, filename_in)
    wb.Close()

    Excel = win32com.client.Dispatch('Excel.Application')
    Excel.Visible = True
    Excel.DisplayAlerts = False
    
    # プログラム3｜エクセルを開く
    filename = filename
    fullpath = os.path.join(os.getcwd(),filename)
    wb = Excel.Workbooks.Open(Filename=fullpath)



# 画面から削除して終了
window.close()                                 



