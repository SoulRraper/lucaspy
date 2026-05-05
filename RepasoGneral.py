#tipos de datos
'''
Caracter : Streng # Variables tipo texto EJ: "Mariano"
Entero : Intager (int) # Variable tipo numero entero EJ: 18
Real   : Float #numero con decimas EJ: 
Logico : boolean # permite solo 2 valores, posibles True o False 

'''

#Declaracion de variables
# print("repaspo general")

# nombre="Diego" 
# edad=64

#Concatenacion
# print("hola", nombre, "su edad es", edad)
# print(f"hola {nombre} y su edad es {edad}")

#Solicitud de variable
# nombre=input("ingrese su nombre: ")
# edad=int(input("ingrese su edad"))


# print(f"hola {nombre} y su edad es {edad}")


# #suma de 2 numeros
# print("ingrese 2 numeros")
# n1=int(input())
# n2=int(input())

# print("la suma de los numeros es", n1+n2)

# explicacion y uso de for

# for i in range(3):
#     print(i+1)

# for i in range(3):
#     print("repeticion" ,i+1)

#pedir al ususario la cantidad de notas
#y generar el promedio de estas

# cant=int(input("ingrrese el numero de notas"))
# suma=0
# for i in range(cant):
#     print("ingrese nota ", i+1)
#     nota=float(input())
#     suma+=nota # suma el valor de nota a la variable suma
#suma=suma+nota #trael el valor actual de suma y le suma la nota, actualizando la suma
# prom=suma/cant
# print("el promedio es ", round(prom,1))

#explicacion y uso de librerias

import random
from random import randint
import time

# num1=random.randint(1,6)
# num2=randint(1,6)
# print(num1,num2)

#explicacion y uso de while
# = es asignacionn, asigna un valor a una variable. EJ: numero=19
# == es comparacion, en otras palabras, comparo 2 valores EJ: numero==9

# num=0

# while num<5:
#  print("hola")
#  num+=1

#clave con intentos infinitos
# clave=4455
# 1234
#4455!=1234 /si por lo tanto, esta afirmacion es verdadera True.
# pasword=int(input("ingresesu password: "))
# while clave!=pasword:
#  print("error; intente nuevamente")
#  pasword=int(input("ingrese su password: "))
# print("bienbenido al sistema")

#clave con solo 3 intentos
# clave=3344
# intentos=3
# password=int(input("ingrese su clave: "))

# while clave!=password or intentos==0:
#  intentos-=1
#  print(f"error, le quedan {intentos} intentos")
#  password=int(input("ingrese su clave :"))
#  if intentos<=1:
#   break

# if intentos!=0 and clave==password:
#  print("usted ingreso al sistema")
# else:
#  print("sistema bloqueado")

#cerrar las ventanas por la cantidad de ventanas en casa
# num=int(input("cuantas ventanas tiene"))


# for i in range (num):
#     print("cierra la ventana")

#recorrer las letras de una frase con un for
# frase=input("ingrese una frase")

# for i in frase:
#     print(i)

#contar los autos que llegan al estacionamiento
#rojos, azules y otro color

# rojos=0
# azules=0
# otro=0
# color=0

# while color!=4:

#     color=int(input('''
#                     ingrese el color del auto
#                     1.- rojo
#                     2.- azul
#                     3.- otro
#                     4.- salir
#                     '''))
#     if color==1:
#         print("el color es rojo")
#         rojos+=1
#     elif color==2:
#         print("el color es azul")
#         azules+=1
#     elif color==3:
#         print("el color es otro")
#         otro+=1
#     else:
#         print("saliendo")

# print("los autos de color rojo son", rojos)
# print("los autos de color azul son", azules)
# print("los autos de otro color son", otro)







#categorizar jugadores
#en una liga amateur, se paga a lo jugadores de futbol
#cuando anota mas goles recibe un bono en su paga
#entre 1-3 goles, 4%; entre 4-6 goles 6%, 7goles o mas 8%
# si su equipo queda entre los 3 primeros, +300
# si su equipo queda entre 4-5, +200
# si su equipo queda entre 9 y mas, +100
# el pago base por jugador es de 5000

# goles=randint(1,10)
# print("los goles anotados en la temporada fueron", goles)
# time.sleep(1)
# pos=randint(1,16)
# print("la possicion final en la temporada fue", pos)
# time.sleep(1)
# # goles=int(input("cuantos goles metio?"))
# sueldo=5000

# if goles>=1 and goles<=3:
#     sueldo=sueldo*1.04
# elif goles>=1 and goles<=6:
#     sueldo=sueldo*1.06
# else:
#     sueldo=sueldo*1.08
# print("el sueldo aumentado es", sueldo)

# if pos>=1 and pos<=3:
#     sueldo+=3000
# elif pos>=4 and pos<=8:
#     sueldo+=2000
# else:
#     sueldo+=1000
# print("el total del sueldo del jugador al final de temporada es", sueldo)
#calcular el arancel a pagar segun grupo familiar y comuna en la que resude
#a continuacion, los descuentos por comuna:
#La florida 20%, la pintana 30%, puente alto 25%, san joaquin 15%
# grupo familiar: 1=>2%, 2 a 4=>, 5 o mas=>4%
# preguntar alm usuario en que comuna vive
# preguntar al usuario con cuantas personas vive
# el arancel actual es de 200.000 por semestre
# basados en la respuesta del usuario y enumeratela informacion dada, calcula su descuento
'''
ej:
ingresar su comuna : la florida
ingresar su grupo familiar(numero entero usted incluido) : 4
el total del descuento es 23%
el total a pagar es $154.000
'''
arancel=200000
descuento=0
print('''
    1.- la florida 20%
    2.- la pintana 30%
    3.- puente alto 25%
    4.- san joaquin 15%
      ''')
comuna=int(input("seleccione su comuna: "))

if comuna==1:
    descuento=20
elif comuna==2:
    descuento=30
elif comuna==3:
    descuento=25
elif comuna==4:
    descuento=15
else:
    print("seleccion incorrecta")

grupo=int(input("ingrese su grupo familiar(numero entero usted incluido) :"))

if grupo==1:
    descuento+=2
elif grupo<=4 and grupo>=2:
    descuento+=3
elif grupo>=5:
    descuento+=4
else:
    print("seleccion incorrecta")

print("el descuento total es ", descuento)
desc=arancel*descuento/100
total=arancel-desc
print("el total a pagar es $" , total) 


