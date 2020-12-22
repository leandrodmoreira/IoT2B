import pymysql.cursors
from connection_package.enviroment import *

timeStamp = '2020-12-22 12:00'
equipament = 1
temperature = 26,6
humidity = 53,7
pressure = 91402
gasResistence = 4992

mysqlConnection(mysqlHost,mysqlUser,mysqlPassword,mysqlDb)

connection = pymysql.connect(host=mysqlHost,
                             user=mysqlUser,
                             password=mysqlPassword,
                             db=mysqlDb,
                             cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        sql = "INSERT INTO `airData` (`timeStamp`, `equipament` , `temperature`, `humidity` , `pressure`, `gasResistence`) VALUES (%s, %s, %s, %s, %s, %s)"
        cursor.execute(sql, (timeStamp, equipament, temperature, humidity, pressure, gasResistence))
    connection.commit()

finally:
    connection.close()