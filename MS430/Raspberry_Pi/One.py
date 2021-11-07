from datetime import datetime
import time
import random
import gspread

from oauth2client.service_account import ServiceAccountCredentials
scope = ['https://spreadsheets.google.com/feeds']
credentials = ServiceAccountCredentials.from_json_keyfile_name('iot2bv2-ebd620022c11.json', scope)
gc = gspread.authorize(credentials)
wks = gc.open_by_key('1CKtNQd9e1RU3ZovV4lix5TSiFR1gIbiHROgVGjOvxVI')
worksheet = wks.get_worksheet(0)

arqCont = open("cont.txt","r")

linha = arqCont.read(100)

contA = 'A' + str(linha)
contB = 'B' + str(linha)

data_e_hora_atuais = datetime.now()
DataHora = data_e_hora_atuais.strftime('%d/%m/%Y %H:%M')

Rvalue = random.randrange(20,30)

worksheet.update_acell(contA, DataHora)
worksheet.update_acell(contB, Rvalue)

linha = int(linha) + 1
arqCont.close()

arqCont = open("cont.txt","w")
arqCont.write(str(linha))
arqCont.close()