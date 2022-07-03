import csv
import sys
from sys import argv
from datetime import datetime

dt = datetime.now()
dtn = dt.strftime("%d-%m-%Y")

n = len(sys.argv)

nombre_csv = sys.argv[1]      
dni = sys.argv[2]
salida = sys.argv[3]
tipo = sys.argv[4]
estado = None
fecha = None

if n == 6:
  estado = sys.argv[5]
  fecha = sys.argv[5]
elif n == 7:
  estado = sys.argv[5]
  fecha = sys.argv[6]

with open (f"{nombre_csv}", "r") as archivo:
    csv_reader = csv.reader(archivo)
    
    for line in csv_reader:   
      if dni in line[8]:      
        if salida == "PANTALLA":
          if tipo in line:
            if estado in line and tipo in line:
              print(line)
            elif estado == None:
              print(line)

                  
        elif salida == "CSV":
          if tipo in line[9]:
            if estado in line and tipo in line[9]:
              with open(f"{dni}-{dtn}.csv", "a") as archivo:
                csv_writer = csv.writer(archivo)
                csv_writer.writerow(line) 
            elif estado == None and tipo in line[9]: 
              with open(f"{dni}-{dtn}.csv", "a") as archivo:
                csv_writer = csv.writer(archivo)
                csv_writer.writerow(line)

        