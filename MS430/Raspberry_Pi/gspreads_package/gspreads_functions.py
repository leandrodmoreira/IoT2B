def gsAirData (timeStamp, equipament, temperature, humidity, pressure, gasResistence):
    import gspread
    from oauth2client.service_account import ServiceAccountCredentials

    scope = ['https://spreadsheets.google.com/feeds']

    credentials = ServiceAccountCredentials.from_json_keyfile_name('/home/pi/Public/Dev/IoT2B/MS430/Raspberry_Pi/gspreads_package/perfect-transit-298617-ae8840d45b6e.json', scope)

    gc = gspread.authorize(credentials)

    #singleAirData Sheet
    wks = gc.open_by_key('1qPT0JHCtQ9cID-0vLi6nqr8F2Db7m0U15Gfna7vBHqU')

    worksheet = wks.get_worksheet(0)

    worksheet.update_acell('A2', timeStamp)
    worksheet.update_acell('B2', equipament)
    worksheet.update_acell('C2', temperature)
    worksheet.update_acell('D2', humidity)
    worksheet.update_acell('E2', pressure)
    worksheet.update_acell('F2', gasResistence)

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