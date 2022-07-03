import csv
import argparse
from datetime import datetime

dt = datetime.now()
dtn = dt.strftime("%d-%m-%Y")

with open ("movimiento_cheques.csv", "r") as archivo:
    csv_reader = csv.reader(archivo)
    for line in csv_reader:

      parser = argparse.ArgumentParser()
      parser.add_argument("DNI", type = str,)
      parser.add_argument("salida", type = str)
      parser.add_argument("tipo", type = str)
      parser.add_argument("estado", type = str, nargs = "?")
      parser.add_argument("rangoFecha", type = str, nargs = "?")
      args = parser.parse_args()

      if args.DNI in line[8]:      
        if args.salida == "PANTALLA":
          if args.tipo in line[9]:
            if args.estado in line and args.tipo in line[9]:
                print(line)
            elif args.estado == None: 
                print(line)
                
      elif args.salida == "CSV":
          if args.tipo in line[9]:
            if args.estado in line and args.tipo in line[9]:
              with open(f"{args.DNI}-{dtn}.csv", "w") as archivo:
               csv_writer = csv.writer(archivo)
               csv_writer.writerow(line) 
            elif args.estado == None and args.tipo in line[9]: 
              with open(f"{args.DNI}-{dtn}.csv", "w") as archivo:
               csv_writer = csv.writer(archivo)
               csv_writer.writerow(line)

        