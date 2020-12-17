#  Part of that code belongs to Metriful Ltd.
#  Licensed under the MIT License - for further details see Metriful Ltd LICENSE.txt file.

from datetime import datetime
import time
import pymysql.cursors
import gspread

from gspreads_package.gspreads_functions import *

now = datetime.now()
timeStamp =  now.strftime('%Y-%m-%d %H:%M')
hosty = 1
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

print("__________________________________________________")
print("Aqui começa meu código")

pressure = air_data['P_Pa']
gasResistence = air_data['G_ohm']

print(temperature)
print(humidity)
print(pressure)
print(gasResistence)

ref_arquivo = open("/home/pi/Public/Dev/IoT2B/MS430/Raspberry_Pi/dbconfig.txt","r")

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
        sql = "INSERT INTO `airData` (`timeStamp`, `equipament` , `temperature`, `humidity` , `pressure`, `gasResistence`) VALUES (%s, %s, %s, %s, %s, %s)"
        cursor.execute(sql, (timeStamp, equipament, temperature, humidity, pressure, gasResistence))
    connection.commit()

finally:
    connection.close()

valor1 = timeStamp
valor2 = id

gsAirData(valor1,valor2)

GPIO.cleanup()