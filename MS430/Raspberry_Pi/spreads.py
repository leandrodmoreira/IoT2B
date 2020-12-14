import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds']

credentials = ServiceAccountCredentials.from_json_keyfile_name('perfect-transit-298617-ae8840d45b6e.json', scope)

gc = gspread.authorize(credentials)

wks = gc.open_by_key('17IaRGDBCB8k5O_HBfpVpc5qnyotOtEq6OR0LhzIRF_o')

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

val = worksheet.cell(1,1).value

print(val)

val = worksheet.col_values(1)

print(val)

val = worksheet.row_values(1)

print(val)

cell = worksheet.find("Florianópolis")

print(f'Encontrado na celula {cell.row} coluna {cell.col}')