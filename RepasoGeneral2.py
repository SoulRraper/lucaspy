#repasoGeneral2
# #ejercicios de random
# import random

# n1=int(input("ingrese el limite inferior: "))
# n2=int(input("ingrese el limite superior: "))

# while n1>n2:
#     print("el segundo numero debe ser superior al primero")
#     n2=int(input("ingrese el limite superior"))        

# rand=random.randint(n1,n2)

# print(rand)

# menus con if

# op=int(input('''
#             Seleccione una opcion
#              1.- opcion1
#              2.- opcion3
#              3.- opcion3
#              '''))

#if con elif
# if op==1:
#     print("has selecionado la opcion 1")
# elif op==2:
#     print("has selecionado la opcion 2")
# elif op==3:
#     print("has selecionado la opcion 3")
# else:
#     print("opcion invalida")

#if secuenciales
# if op==1:
#     print("has seleccionado la opcion 1")
# if op==2:
#     print("has seleccionado la opcion 2")
# if op==3:
#     print("has seleccionado la opcion 3")


#verificacion de clave secreta, intentos infinitos
# clave=9988

# while True:
#     passw=int(input("ingrese su clave: "))
#     if clave==passw:
#         break
#     print("clave invalida")
# print("clave aceptada")

# #verificacion de clave secreta, 3 intentos
# clave=9988
# intentos=3

# while intentos !=0:
#     intentos-=1
#     passw=int(input("ingrese su clave: "))
#     if clave==passw:
#         break
#     print(f"clave invalida, te quedan {intentos} intentos")
# if clave!=passw:
#     print("se le acabaron los intentos, ususario bloqueado")
# else:
#   print("clave aceptada")

# #uso de match

# op=int(input('''
#             Seleccione una opcion
#              1.- opcion1
#              2.- opcion3
#              3.- opcion3
#              '''))

# match op:
#     case 1:
#          print("has seleccionado la opcion 1")
#     case 2:
#          print("has seleccionado la opcion 2")
#     case 3:
#          print("has seleccionado la opcion 3")
#     case _:
#         print("opcion invalida")

# manejo de error para evitar la caida del programa

# while True:
#     try:
#         #codigo a implementar
#         num=float(input("ingrese un numero: "))
#         print("el numero ingresado es", num)
#         break
#     except Exception:
#         # respuesta en caso de error
#         print("solo debe ingresar numeros ")

#VOTATON
#designe 2 candidatos, pregunte cuanto votantes son
#por cada votante, debe preguntar por quien votara
# #cuente la cantidad de votos y muestra los resultados
# # definir quien gano la votacion considere empate

# c1="un show mas"
# c2="hora de aventura"
# cv1=0
# cv2=0

# cantV=int(input("cuantos votantes son? "))

# for i in range(cantV):
#     print(f"por quien votara? 1.- {c1}, 2.- {c2} ")
#     voto=int(input())
#     if voto==1:
#         cv1=cv1+1
#         #cv1+=1
#     else:
#         cv2=cv2+1
# print(f"la cantidad de votos de {c1} es {cv1}")
# print(f"la cantidad de votos de {c2} es {cv2}")
# if cv1>cv2:
#     print(f"gano {c1}")
# elif cv1<cv2:
#     print(f"gano {c2}")
# else:
#     print("es un empate")


# ejercicio de for

# poner la mesa

import time
familia=int(input("cuantos familiares son: "))
jugo=1000
comida=700

for i in range(familia):
    print("poner plato")
    time.sleep(1)
    print("poner servicio")
    time.sleep(1)
    print("poner vaso")
    time.sleep(1)
    if jugo>200:
        print("llena el vaso")
        jugo-=200
        print(f"queda {jugo} de jugo")
        time.sleep(2)
    else:
        print("no queda jugo")
    if comida>500:
        print("llena el plato")
        comida-=500
        print(f"queda {comida} de comida")
        time.sleep(2)
    else:
        print("no queda comida")

#poner la mesa con un while

import time
familia=int(input("cuantos familiares son: ")) # 2
jugo=1000
comida=700
puestos=0

while familia>puestos:
    print("poner plato")
    time.sleep(1)
    print("poner servicio")
    time.sleep(1)
    print("poner vaso")
    time.sleep(1)
    if jugo>200:
        print("llena el vaso")
        jugo-=200
        print(f"queda {jugo} de jugo")
        time.sleep(2)
    else:
        print("no queda jugo")
    if comida>500:
        print("llena el plato")
        comida-=500
        print(f"queda {comida} de comida")
        time.sleep(2)
    else:
        print("no queda comida")
    puestos+=1