import barcode
from barcode.writer import ImageWriter
codeClass = barcode.get_barcode_class('code128')
from sys import exit
import random, string, os, sys, shutil, datetime, pathlib


pathname = os.path.dirname(sys.argv[0])
fullPath = os.path.abspath(pathname)
pathGen= fullPath+"\Generados"

if not os.path.exists(pathGen):
    try:
        os.mkdir(pathGen)
    except OSError:
        print ("Falla en la creacion del directorio 'Generados', intente crearlo manualmente")
        ex = input()
        exit()
    else:
        print ("Se ha creado el directorio 'Generados', en el se guardaran los codigos creados ")


print("Ingrese 1 Para generar codigos aleatoriamente, 2 para generarlos a partir de un archivo de texto .txt ")
try:
    n = int(input())

except ValueError:
      print ("Entrada no válida")
      ex = input()
      exit()

if (n==1):
    print("Ingrese el numero de codigos a generar: ")
    try:
        numCodigos = int(input())
        print("Generando...")
        fecha = datetime.datetime.now()
        with open("Generados.txt", 'w') as out:
             out.write("Codigos generados "+str(fecha)+ '\n')
        shutil.move("Generados.txt" , "Generados/Generados.txt")

        for p in range (0,numCodigos):
            x = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
            print(x)
            output = codeClass(x, writer=ImageWriter())
            name = x
            fullname = output.save(name)
            #Move files
            current = (name+".png")
            new = ("Generados/"+name+".png")
            shutil.move(current , new)
            with open("Generados/Generados.txt", 'a') as out:
                 out.write(x + '\n')

        print ("Exito. Se generaron "+str(numCodigos)+" codigos")
        ex = input()
        exit()

    except ValueError:
          print ("Entrada no válida")
          ex = input()
          exit()


if (n==2):

    datadir = 'archivo.txt'
    try:
        with open(datadir,"r") as inputFile:
             data = inputFile.read().splitlines()
             print (data)
             print ("Generando Codigos. Por favor espere...")
             for i in range(0, len(data)):
                 output = codeClass(data[i], writer=ImageWriter())
                 name = data[i]
                 fullname = output.save(name)

                 #Move files
                 current = (name+".png")
                 new = ("Generados/"+name+".png")
                 shutil.move(current , new)

        print ("Exito. Se generaron "+str(len(data))+" codigos")
        ex = input()
        exit()


    except IOError:
          print ("Error: El archivo no existe.")
          ex = input()
          exit()


if(n!=1 and n!=2):
    print("El numero ingresado no es válido")
    ex = input()
    exit()
