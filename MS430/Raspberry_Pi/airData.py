#  Part of that code belongs to Metriful Ltd.
#  Licensed under the MIT License - for further details see Metriful Ltd LICENSE.txt file.

from datetime import datetime
import time
import pymysql.cursors
import gspread

#from gspreads_package.gspreads_functions import *

now = datetime.now()
timeStamp =  now.strftime('%Y-%m-%d %H:%M')
equipament = 1

from sensor_package.sensor_functions import *

# Set up the GPIO and I2C communications bus
(GPIO, I2C_bus) = SensorHardwareSetup()

# Initiate an on-demand data measurement
I2C_bus.write_byte(i2c_7bit_address, ON_DEMAND_MEASURE_CMD)

# Now wait for the ready signal (falling edge) before continuing
while (not GPIO.event_detected(READY_pin)):
  sleep(0.05)
  
air_data = get_air_data(I2C_bus)

# Get the data from the MS430
raw_data = I2C_bus.read_i2c_block_data(i2c_7bit_address, H_READ, H_BYTES)

# Decode the humidity: the first received byte is the integer part, the 
# second byte is the fractional part (to one decimal place).
humidity = raw_data[0] + float(raw_data[1])/10.0

# Get the data from the MS430
raw_data = I2C_bus.read_i2c_block_data(i2c_7bit_address, T_READ, T_BYTES)

# Find the positive magnitude of the integer part of the temperature by 
# doing a bitwise AND of the first received byte with TEMPERATURE_VALUE_MASK
temp_positive_integer = raw_data[0] & TEMPERATURE_VALUE_MASK

# The second received byte is the fractional part to one decimal place
temp_fraction = raw_data[1]

# Combine to form a positive floating point number:
temperature = temp_positive_integer + float(temp_fraction)/10.0

# Now find the sign of the temperature: if the most-significant bit of 
# the first byte is a 1, the temperature is negative (below 0 C)
if ((raw_data[0] & TEMPERATURE_SIGN_MASK) != 0):
  # The bit is a 1: temperature is negative
  temperature = -temperature

#writeAirData(None, air_data, False)

pressure = air_data['P_Pa']
gasResistence = air_data['G_ohm']

ref_arquivo = open("/home/pi/Public/dev/IoT2B/MS430/Raspberry_Pi/dbconfig.txt","r")

for linha in ref_arquivo:
    valores = linha.split()
    host = valores[0].replace(",","")
    user = valores[1].replace(",","")
    password = valores[2].replace(",","")
    db = valores[3].replace(",","")

ref_arquivo.close()

#Gravando dados no banco de dados
connection = pymysql.connect(host=host,
                             user=user,
                             password=password,
                             db=db,
                             cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        sql = "INSERT INTO `airData` (`timeStamp`, `equipament` , `temperature`, `humidity` , `pressure`) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(sql, (timeStamp, equipament, temperature, humidity, pressure))
    connection.commit()

finally:
    connection.close()

#gsAirData(timeStamp, equipament, temperature, humidity, pressure, gasResistence)

from oauth2client.service_account import ServiceAccountCredentials
scope = ['https://spreadsheets.google.com/feeds']
credentials = ServiceAccountCredentials.from_json_keyfile_name('/home/pi/Public/dev/IoT2B/MS430/Raspberry_Pi/iot2bv2-ebd620022c11.json', scope)
gc = gspread.authorize(credentials)
wks = gc.open_by_key('1Sjq3HmkMCt6LhME6F9rhteMYT1DlhseJwpMEFZc5qU4')
worksheet = wks.get_worksheet(0)

arqCont = open("/home/pi/Public/dev/IoT2B/MS430/Raspberry_Pi/cont.txt","r")
linha = arqCont.read(100)
print(linha)

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

#arqCont = open("cont.txt","w")
arqCont = open("/home/pi/Public/dev/IoT2B/MS430/Raspberry_Pi/cont.txt","w")
arqCont.write(str(linha))
arqCont.close()

GPIO.cleanup()

#Teste