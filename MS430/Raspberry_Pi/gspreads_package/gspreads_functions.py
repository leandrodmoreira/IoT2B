def gsAirData (valor1,valor2):
    import gspread
    from oauth2client.service_account import ServiceAccountCredentials

    scope = ['https://spreadsheets.google.com/feeds']

    credentials = ServiceAccountCredentials.from_json_keyfile_name('perfect-transit-298617-ae8840d45b6e.json', scope)

    gc = gspread.authorize(credentials)

    #Planilha Teste Python
    wks = gc.open_by_key('17IaRGDBCB8k5O_HBfpVpc5qnyotOtEq6OR0LhzIRF_o')

    worksheet = wks.get_worksheet(0)

    worksheet.update_acell('A1', valor1)
    worksheet.update_acell('B1', valor2)



def soma(A,B):
  C = A + B
  print('C =', C)
  return C

