# Importacion de librerias
import pickle
import argparse
import random
import sys
import time
import threading 

#Declaraion de variable 

# Declaracion de funciones

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--x",type= int,default=0,help="Elija el tamaño del array")
    parser.add_argument("--Formato",type= int,default=0,help="Elija el formato de impresion")
    args=parser.parse_args()
    sys.stdout.write(str(Tarea2(args)))

def cuadrado(lista,listaaux,salida):
    i=listaaux[0]
    while i<=listaaux[-1]:
        salida.append(lista[i]**2)
        i+=1
        time.sleep(0.0001)
    

def Tarea2(args):
    lista=[]
    listaaux=[]
    lista1Th=[]
    
    i=0
    while(i<args.x):
        lista.append(random.randint(1,10))
        listaaux.append(i)
        i+=1

    inicio=time.time()
    cuadrado(lista,listaaux,lista1Th)
    fin=time.time()

    print("La duracion con un hilo es de: ",fin-inicio," s")

    lista4Th1=[]
    lista4Th2=[]
    lista4Th3=[]
    lista4Th4=[]
    inicio2=time.time()
    t1=threading.Thread(target=cuadrado,args=(lista, listaaux[0*args.x//4:(0+1)*args.x//4], lista4Th1))
    t1.start()
    t2=threading.Thread(target=cuadrado,args=(lista, listaaux[1*args.x//4:(1+1)*args.x//4], lista4Th2))
    t2.start()
    t3=threading.Thread(target=cuadrado,args=(lista, listaaux[2*args.x//4:(2+1)*args.x//4], lista4Th3))
    t3.start()
    
    t4=threading.Thread(target=cuadrado,args=(lista, listaaux[3*args.x//4:(3+1)*args.x//4], lista4Th4))
    t4.start()
    t4.join()
    fin2=time.time()
    print("La duracion con 4 hilos es de: ",fin2-inicio2,"s")
    listanueva=[]
    listanueva+=lista4Th1
    listanueva+=lista4Th2
    listanueva+=lista4Th3
    listanueva+=lista4Th4
    if (args.Formato==0):
        print("La lista de numeros es\n")
        print(lista,"\n")
        print("La lista de numeros al cuadrado es\n")
        print(listanueva)
    else:
        s=listanueva
        listToStr = ' '.join([str(elem) for elem in s])
        s=lista
        listToStr1 = ' '.join([str(elem) for elem in s])
        ficheros=open("Numeros al cuadrado","w")

        ficheros.write("La lista de numeros es\n")
        ficheros.write(listToStr1)
        ficheros.write("\n")
        ficheros.write("La lista de numeros al cuadrado es\n")
        ficheros.write(listToStr)
        ficheros.close()
        del(ficheros)
        print("Se realizo un archivo .txt con los resultados")


if __name__=="__main__":
    main()