import csv
import sys
from sys import argv
from datetime import date, datetime

n = len(sys.argv)

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
 
filtrados = set()     
for nro_line, line in enumerate(res):
   nro_cheque = line[0]
   nro_cuenta = line[3]
   nro_dni = line[8]

if(nro_cheque, nro_cuenta, nro_dni) in filtrados:
  res.append(f"Hay datos repetidos en fila {nro_line}")
else:
  filtrados.add((line[0], line[3], line[8]))
                       
if salida == "PANTALLA":
  for fila in res:
    print(",".join(fila))
    
elif salida == "CSV":
    datos = [[line[3], line[5], line[6], line[7]]for line in res]
    dt = datetime.now()
    dt = dt.strftime("%d,%m,%Y")
    with open(f"{dni}-{dt}.csv", "w", newline="") as archivo:
        writer = csv.writer(archivo)
        writer.writerows(datos)
  

        