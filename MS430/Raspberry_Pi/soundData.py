#  Part of that code belongs to Metriful Ltd.
#  Licensed under the MIT License - for further details see Metriful Ltd LICENSE.txt file.

from datetime import datetime
import time
import pymysql.cursors
#from gspreads_package.gspreads_functions import *

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

sound_data = get_sound_data(I2C_bus)

# Get the data from the MS430
raw_data = I2C_bus.read_i2c_block_data(i2c_7bit_address, H_READ, H_BYTES)

#writeSoundData(None, sound_data, False)

aWeightedSPL = sound_data['SPL_dBA']
freqBand1 = sound_data['SPL_bands_dB'][0]
freqBand2 = sound_data['SPL_bands_dB'][1]
freqBand3 = sound_data['SPL_bands_dB'][2]
freqBand4 = sound_data['SPL_bands_dB'][3]
freqBand5 = sound_data['SPL_bands_dB'][4]
freqBand6 = sound_data['SPL_bands_dB'][5]
peakSA = sound_data['peak_amp_mPa']
stable = sound_data['stable']

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
        sql = "INSERT INTO `soundData` (`timeStamp`, `equipament`, `aweightedSPL`, `freqBand1`, `freqBand2`, `freqBand3`, `freqBand4`, `freqBand5` ,`freqBand6`, `peakSA`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(sql, (timeStamp, equipament, aWeightedSPL, freqBand1, freqBand2, freqBand3, freqBand4, freqBand5, freqBand6, peakSA))
    connection.commit()

finally:
    connection.close()

#gsSoundData (timeStamp, equipament, aWeightedSPL, freqBand1, freqBand2, freqBand3, freqBand4, freqBand5, freqBand6, peakSA)

GPIO.cleanup()