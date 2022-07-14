import csv
import sys
from sys import argv
from datetime import date, datetime

n = len(sys.argv)
if (n < 5):
  print("¡Ingresar 4 argumentos como mínimo!")
  print("El orden de los argumentos son los siguientes:\
    \n  a. Nombre del archivo csv\
    \n  b. DNI del cliente\
    \n  c. Salida: PANTALLA o CSV\
    \n  d. Tipo de cheque: EMITIDO o DEPOSITADO\
    \n  e. Estado del cheque: PENDIENTE, APROBADO, RECHAZADO (Opcional)\
    \n  f. Rango de fecha: xx-xx-xxxx:yy-yy-yyyy (Opcional)")
  sys.exit()   
if (n>7):
  print("¡Error! Se pueden ingresar hasta 6 parametros (4 obligatorios y 2 opcionales)")
  sys.exit()

nombre_csv = sys.argv[1]      
dni = sys.argv[2]
salida = sys.argv[3]
tipo = sys.argv[4]
estado = None
fecha = None

if n == 6:
  opcional = sys.argv[5]
  estados = ["PENDIENTE", "APROBADO", "RECHAZADO"]
  if opcional in estados:
    estado = opcional
  else:
    fecha = opcional.split(":")

elif n == 7:
  estado = sys.argv[5]
  fecha = sys.argv[6].split(":")

if fecha:
  fecha_inicial = datetime.timestamp(datetime.strptime(fecha[0], "%d-%m-%y"))
  fecha_final = datetime.timestamp(datetime.strptime(fecha[1], "%d-%m-%y"))
  
res = []

with open (f"{nombre_csv}", "r") as archivo:
    csv_reader = csv.reader(archivo, delimiter=",")
    
    for line in csv_reader:
      dni_cheque = line[8]
      tipo_cheque = line[9]
      estado_cheque = line[10]  
      fecha_cheque = line[6]
       
      if dni_cheque != dni or tipo_cheque != tipo:
        continue
      if estado and estado_cheque != estado:
        continue      
      if fecha and (fecha_cheque < fecha_inicial or fecha_cheque > fecha_final):
        continue
      res.append(line)

#Filtrado nuevo             
def Repetidos():
  repetidos = []
  no_repetidos = []
  for line in res:
    numero_cheque = line[0]
    if numero_cheque not in no_repetidos:
      no_repetidos.append(numero_cheque)
    elif numero_cheque not in repetidos:
      repetidos.append(numero_cheque)
  if len(repetidos) == 0:
    return False
  else:
    for error in repetidos:
      print(f'¡Error! El cheque N° {error} con DNI: {dni}, está repetido')

                       
if salida == "PANTALLA":
  Repetidos()
  for fila in res:
    print(",".join(fila))
elif salida == "CSV":
  Repetidos()
  datos = [[line[3], line[5], line[6], line[7]]for line in res]
  dt = datetime.now()
  dt = dt.strftime("%d,%m,%Y")
  with open(f"{dni}-{dt}.csv", "w", newline="") as archivo:
    writer = csv.writer(archivo)
    writer.writerows(datos)

  

        