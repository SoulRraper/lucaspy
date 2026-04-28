#uso y ejemplos de random

import random
# num=random.randint(1,10)
# print(num) 

# for i in range(num):
#     print("hola deny")

# dado1=random.randint(1,6)
# dado2=random.randint(1,6)

# print(f"el dado 1 dio {dado1}")
# print(f"el dado 2 dio {dado2}")

# if dado1==dado2:
#     print("se va a la carcel")
# else:
#     print("avanza prfavor")

# crea un numero random entre 1 y 100
# pide al ususario que adivine el numero
# si el ususario pone un numero mayor al generado
# debe decir "te pasaste" , en caso contrario
# " el numero a adivinar es mayor"
# solo hay 5 posibilidades de adivinar.

# import random
# numrandom=random.randint(1,100)

# for intento in range(5):
#  adivina = int(input("adivina entre 1 y 100: "))

# if adivina== numrandom :
#     print("correcto adivinaste")
#     break
# elif adivina>numrandom:
#    print("te pasaste")   
# else:
#    print("el numero a adivinar es mayor")
# else:
#  print(f"se acabaron los intentos. el numero era {numrandom}")


# import random
import time
# posicion=0
# turnos=0
# meta=30

# print("mi ludo")
# print("llega a la casilla 30 para ganar")

# while posicion<meta:
#     print("lanzar los dados")
#     turnos+=1

#     dado1=random.randint(1,6)
#     dado2=random.randint(1,6)
#     avance=dado1+dado2

#     posicion+=avance
#     time.sleep(1)
#     print(f"lanzaste:{dado1} y {dado2}")
#     print(f"avanzas {avance} casillas")
#     print(f"estas en la casilla: {posicion}/{meta}")

# print(f"ganaste llegaste a la meta en {turnos} turnos")

j1=random.randint(60,190)
j2=random.randint(60,190)
j3=random.randint(60,190)

print(f"el jugador 1 lanzo la pelota {j1} metros")
print(f"el jugador 1 lanzo la pelota {j2} metros")
print(f"el jugador 1 lanzo la pelota {j3} metros")

if j1>j2 and j1>j3:
    print("el jugador uno, lanzo la pelota mas lejos")
elif j2>j3:
    print("el jugador dos, lanzo la pelota mas lejos")
elif j1==j2==j3:
    print("los tres mandaron la pelota a la misma distancia")
else:
    print("el jugador tres, lanzo la pelota mas lejos")
   
