def gsAirData (timeStamp, equipament, temperature, humidity, pressure, gasResistence):
    import gspread
    from oauth2client.service_account import ServiceAccountCredentials

    scope = ['https://spreadsheets.google.com/feeds']

    credentials = ServiceAccountCredentials.from_json_keyfile_name('/Public/Dev/IoT2B/MS430/Raspberry_Pi/gspreads_package/perfect-transit-298617-ae8840d45b6e.json', scope)

    gc = gspread.authorize(credentials)

    #Planilha Teste Python
    wks = gc.open_by_key('17IaRGDBCB8k5O_HBfpVpc5qnyotOtEq6OR0LhzIRF_o')

    worksheet = wks.get_worksheet(0)

    worksheet.update_acell('A2', timeStamp)
    worksheet.update_acell('B2', equipament)
    worksheet.update_acell('C2', temperature)
    worksheet.update_acell('D2', humidity)
    worksheet.update_acell('E2', pressure)
    worksheet.update_acell('F2', gasResistence)



def soma(A,B):
  C = A + B
  print('C =', C)
  return C

