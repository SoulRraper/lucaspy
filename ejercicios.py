#loteria
#generar 3 numeros entre 1 y 9
#luego, tirar numeros al azar en ese rango
#cuando todos los numeros coincidan con los primeros 3
#ganadores, debe poner "ganaste"
#contar . cuantos numeros tuvo que tirar
# para ganar la loteria

import random
import time
# n1=random.randint(1,9)
# n2=random.randint(1,9)
# n3=random.randint(1,9)
# t1=False
# t2=False
# t3=False
# nums=0
# print(f"los numeros generados son: {n1}, {n2}, {n3}")
# while not t1 or not t2 or not t3 :
#     numerito=random.randint(1,9)
#     print("el numero es" , numerito )
#     time.sleep(1)
#     if numerito==n1 :
#         t1=True
#     if numerito==n1 :
#         t2=True
#     if numerito==n1 :
#         t3=True
#     nums+=1
# print(f"ganaste, {nums} turnos")

'''
fabrica de enlatados
se necesita hacer el algoritmo de productos enlatados
se debe consultar el peso del producto (en gramos) (solo valores positivos)
el porcentaje de sodio en el (solo valores entre 1 y 100)
y si se va avender nacional o internacionalmente
considera los criterios en la siguiente tabla

menos 500 grs, lata normal
501 hassta 1500 bgr, lata mediana
1501 y mas, lata grande
si el sodio es menos de 5%, la lata queda igual
si es entre 5% y 8% la lata especial
si tiene 9% o mas, lata acorazada
a las latas internacionales, se le debbe pegar
un sticker de validacion sanitaria

ej:800, 7%, lima==> lata mediana especial con sticker sanitario
'''
peso=float(input("peso en gramos: "))
sodio=float(input("porcentaje de sodio: "))
mercado=input("mercado nacional o internacional: ")

    
if peso < 500 :
    tipolata = " lata normal "
elif peso <= 1500 :
    tipolata = " lata mediana "
else:
    tipolata = " lata grande "
    
if sodio < 5 :
   especialidad = ""
elif sodio <= 8 :
   especialidad = " especial "
else:
   especialidad = " acorazada "

sticker = ""
if mercado == " internacional ":
    sticker = " con sticker sanitario "

print(tipolata+especialidad+sticker)

# version sin float
# peso=int(input("peso en gramos: "))
# sodio=int(input("porcentaje de sodio: "))
# mercado=input("mercado nacional o internacional: ")

    
# if peso < 500 :
#     tipolata = " lata normal "
# elif peso <= 1500 :
#     tipolata = " lata mediana "
# else:
#     tipolata = " lata grande "
    
# if sodio < 5 :
#    especialidad = ""
# elif sodio <= 8 :
#    espeialidad = " especial "
# else:
#    especialidad = " acorazada "

# sticker = ""
# if mercado == " internacional ":
#     sticker = " con sticker sanitario "

# print(tipolata + especialidad+ sticker)