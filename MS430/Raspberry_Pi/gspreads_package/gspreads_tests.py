import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds']

credentials = ServiceAccountCredentials.from_json_keyfile_name('/home/leandro/Documents/Dev/GoogleSheets/perfect-transit-298617-ae8840d45b6e.json', scope)

gc = gspread.authorize(credentials)

#Planilha Teste Sheet
wks = gc.open_by_key('1oLARvIRy09EXD6ST0eWh4oAqQBzYI88kosaOAaBBlNs')

worksheet = wks.get_worksheet(0)

worksheet.update_acell('A1', 'Estado')
worksheet.update_acell('B1', 'Capital')

#Dicionario com os estados e as capitais
capitais = {'Paraíba': 'João Pessoa', 'Santa Catarina': 'Florianópolis', 'São Paulo' : 'São Paulo' }

#Contador de colunas e celulas
colums = 1
cel = 2

for estado, capital in capitais.items():

    #Atualiza a celula 2 da coluna 1 com o nome do estado 
    worksheet.update_cell(cel, colums,estado)
    #A coluna agora é a B
    colums = 2
    #Atualiza a celula 2 da coluna 2 com o nome da capital
    worksheet.update_cell(cel, colums,capital)
    #A coluna agora é a A
    colums = 1 
    #Acrescenta mais um valor no numero da celula
    cel += 1
