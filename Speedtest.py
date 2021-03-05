# -*- coding: utf-8 -*-
from speedtes import speedtest 
from datetime import datetime
import time
import pymysql.cursors

speed = speedtest.Speedtest()
speed.get_best_server()

#Criação das variáveis
now = datetime.now()
timestamp =  now.strftime('%Y-%m-%d %H:%M')
equipament = 1
download = repr(round(speed.download() / 1000 / 1000, 1))
upload = repr(round(speed.upload () / 1000 / 1000, 1))


downloadComma = download.replace(".",",")
uploadComma = upload.replace(".",",")

#Lendo configurações do arquivo

ref_arquivo = open("/home/leandro/Documents/Dev/Velocidade/dbconfig.txt","r")

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
        sql = "INSERT INTO `iot_speedtest` (`timestamp`, `equipament` , `download` , `upload`) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (now, equipament, downloadComma, uploadComma))
    connection.commit()

finally:
    connection.close()

#Gravando dados no arquivo de log
reader = "Timestamp, Download(Mbs), Upload(Mbps) \n"

textoBruto = now.strftime('%Y-%m-%d %H:%M') + ';' + download + ';' + upload + "\n"

texto = textoBruto.replace(".",",")

print("Valor armazenado no banco de dados:")
print(texto)