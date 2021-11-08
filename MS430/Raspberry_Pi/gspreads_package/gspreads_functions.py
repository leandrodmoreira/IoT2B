def gsAirData (timeStamp, equipament, temperature, humidity, pressure, gasResistence):
    import gspread

    from google.oauth2.service_account import ServiceAccountCredentials
    scope = ['https://spreadsheets.google.com/feeds']
    credentials = ServiceAccountCredentials.from_json_keyfile_name('iot2bv2-ebd620022c11.json', scope)
    gc = gspread.authorize(credentials)
    wks = gc.open_by_key('1CKtNQd9e1RU3ZovV4lix5TSiFR1gIbiHROgVGjOvxVI')
    worksheet = wks.get_worksheet(0)

    arqCont = open("cont.txt","r")
    linha = arqCont.read(100)

    contA = 'A' + str(linha)
    contB = 'B' + str(linha)
    contC = 'C' + str(linha)
    contD = 'D' + str(linha)
    contE = 'E' + str(linha)
    contF = 'F' + str(linha)

    worksheet.update_acell(contA, timeStamp)
    worksheet.update_acell(contB, equipament)
    worksheet.update_acell(contC, temperature)
    worksheet.update_acell(contD, humidity)
    worksheet.update_acell(contE, pressure)
    worksheet.update_acell(contF, gasResistence)

    linha = int(linha) + 1
    arqCont.close()

    arqCont = open("cont.txt","w")
    arqCont.write(str(linha))
    arqCont.close()

def gsLightData (timeStamp, equipament, illuminance, whiteLightLevel):
    import gspread
    from oauth2client.service_account import ServiceAccountCredentials

    scope = ['https://spreadsheets.google.com/feeds']

    credentials = ServiceAccountCredentials.from_json_keyfile_name('/home/pi/Public/Dev/IoT2B/MS430/Raspberry_Pi/gspreads_package/perfect-transit-298617-ae8840d45b6e.json', scope)

    gc = gspread.authorize(credentials)

    #singleLightData Sheet
    wks = gc.open_by_key('13NA7k2DcbpV22PRfGidvw-zqeLpwhJd7ccJRBny1pFU')

    worksheet = wks.get_worksheet(0)

    worksheet.update_acell('A2', timeStamp)
    worksheet.update_acell('B2', equipament)
    worksheet.update_acell('C2', illuminance)
    worksheet.update_acell('D2', whiteLightLevel)

def gsSoundData (timeStamp, equipament, aWeightedSPL, freqBand1, freqBand2, freqBand3, freqBand4, freqBand5, freqBand6, peakSA):
    import gspread
    from oauth2client.service_account import ServiceAccountCredentials

    scope = ['https://spreadsheets.google.com/feeds']

    credentials = ServiceAccountCredentials.from_json_keyfile_name('/home/pi/Public/Dev/IoT2B/MS430/Raspberry_Pi/gspreads_package/perfect-transit-298617-ae8840d45b6e.json', scope)

    gc = gspread.authorize(credentials)

    #singleSoundData Sheet
    wks = gc.open_by_key('16VVC1OwdxOsBD3CMRFNpe1gvpgrxIiNJgWN5i9AtN1s')

    worksheet = wks.get_worksheet(0)

    worksheet.update_acell('A2', timeStamp)
    worksheet.update_acell('B2', equipament)
    worksheet.update_acell('C2', aWeightedSPL)
    worksheet.update_acell('D2', freqBand1)
    worksheet.update_acell('E2', freqBand2)
    worksheet.update_acell('F2', freqBand3)
    worksheet.update_acell('G2', freqBand4)
    worksheet.update_acell('H2', freqBand5)
    worksheet.update_acell('I2', freqBand6)
    worksheet.update_acell('J2', peakSA)