#Escribe un programa en Python que muestre la hora actual con una suma de dos horas adicionales
from datetime  import datetime
from datetime import timedelta


fecha = datetime.now()
horas2 = fecha + timedelta(hours=2)
hora = horas2.strftime("%H:%M")
print('La suma de 2 horas a la hora actual es de: ',hora)