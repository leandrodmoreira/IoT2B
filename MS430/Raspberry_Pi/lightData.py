#  Part of that code belongs to Metriful Ltd.
#  Licensed under the MIT License - for further details see Metriful Ltd LICENSE.txt file.

from datetime import datetime
import time
import pymysql.cursors

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

light_data = get_light_data(I2C_bus)

# Get the data from the MS430
raw_data = I2C_bus.read_i2c_block_data(i2c_7bit_address, H_READ, H_BYTES)

writeLightData(None, light_data, False)

illuminance = light_data['illum_lux']
whiteLightLevel =  light_data['white']

print(illuminance)
print(whiteLightLevel)

GPIO.cleanup()