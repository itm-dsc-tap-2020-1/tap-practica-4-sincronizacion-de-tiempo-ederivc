import datetime
import os
from time import ctime
import ntplib

servidor = "time-e-g.nist.gov"
cliente = ntplib.NTPClient()

tiempo1 = datetime.datetime.now()

respuesta = cliente.request(servidor)
horaServidor = datetime.datetime.strptime(ctime(respuesta.tx_time), "%a %b %d %H:%M:%S %Y")

tiempo2 = datetime.datetime.now()

ajuste = (tiempo2-tiempo1)/2
reloj = horaServidor + ajuste

print("\nHora de inicio de la peticion: "+str(tiempo1))
print("Hora de llegada de la peticion: "+str(tiempo2))
print("Servidor: "+str(horaServidor))
print("Ajuste: "+str(ajuste))
print("Reloj: "+str(reloj))

os.system(f"date --set '{reloj}'")
