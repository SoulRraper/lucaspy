# op=0
# total=0
# while op!=4:
#   print("1._pc $500.000")
#   print("2._LGTV SS $450.000")
#   print("3._Microondas Mademsa $100.000")
#   print("4.- salir")
#   print("seleccione una opcion")
#   op=int(input())
#   match op:
#     case 1:
#         print("el total a pagar es" , 500000*1.19)
#         total+=500000-1.19
#     case 2:
#         print("el total a pagar es" , 450000*1.19)
#         total+=450000-1.19
#     case 3:
#         print("el total a pagar es" , 100000*1.19) 
#         total+=100000-1.19
#     case 4:
#         print("saliendo")
#         print("el total a pagar es" , total)
#     case _:
#         print("opcion invalida")

# Calculadora
# + - * /
# def suma():
#  n1=int(input("ingrese un numero"))
#  n2=int(input("ingrese otro numero"))
#  print(f"el resultado es{n1+n2}")

# def resta():
#  n1=int(input("ingrese un numero"))
#  n2=int(input("ingrese otro numero"))
#  print(f"el resultado es{n1-n2}")

# def multiplicacion():
#   n1=int(input("ingrese un numero"))
#   n2=int(input("ingrese otro numero"))
#   print(f"el resultado es{n1*n2}")

# def division():
#   n1=int(input("ingrese un numero"))
#   n2=int(input("ingrese otro numero"))
#   print(f"el resultado es{n1/n2}")

# def calculadora():        
#     op=0
#     while op!=5:
#         print("1.- suma")
#         print("2.- resta")
#         print("3.- multiplicacion")
#         print("4.- division")
#         print("5- salir")
#         print("seleccione una opcion")
#         op=int(input())
#         match op:
#             case 1:
#              suma()
#             case 2:
#              resta()
#             case 3:
#              multiplicacion()
#             case 4:
#              division()
#             case 5:
#              print("saliendo")


# def tablademultiplicar ():
#   num=int(input("ingre un num: "))
#   for i in range(10):
#     print(num , "*" , i+1, "=", num*(i+1))

# def nombre():
#   print("ingrese su nombre")
# nombre=input
# print("hola", nombre)

# def pin():
#   pin=int(input("crea un PIN de 4 digitos: "))

#   if pin>1000 and pin <999:
#      print("Pin creado")
#   else:
#      print("Pin invalido")

#   if len(str()):
#      print("Pin creado")
#   else:
#      print("Pin invalido")

   

# def programas():        
#      op=0
#      while op!=4:
#          print("1.- tabla de multiplicar")
#          print("2.- nombre")
#          print("3.- pin ")
#          print("4.- salir ")         
#          print("seleccione una opcion")
#          op=int(input())
#          match op:
#              case 1:
#               tablademultiplicar()
#              case 2:
#               nombre()
#              case 3:
#               pin()
#              case 4:
#               print("saliendo")
# programas()

# op=0
# cantPersonas=0 #contar la cant de personas que ingresan al zoo
# total=0 # total a pagar por las entradas
# while op!=4:
#    print('''
#      1.- Niño (1-17) $1.000
#      2.- Adulto (18-64) $3.000
#      3.- Adulto mayor  (64 o mas) $1.500
#      4.- salir''' )
#    op=int (input("seleccione una opcion: "))
#    match op:
#       case 1:
#          #preguntar cuantos son en cada persona
#          print("pagando el precio de niño:")
#          c=int(input("cuantos son?: "))
#          #limitar la cant de personas de 1 a 10
#          while c<1 or c<10:
#             print("cantidad fuera de rango")
#             c=int(input("¿cuantos son?"))
#          total+=1000*c
#          cantPersonas+=c
#       case 2:
#          #preguntar cuantos son en cada persona
#          print("pagando el precio de adulto:")
#          c=int(input("cuantos son?: "))
#           #limitar la cant de personas de 1 a 10
#          while c<1 or c<10:
#             print("cantidad fuera de rango")
#             c=int(input("¿cuantos son?"))
#          total+=3000*c
#          cantPersonas+=c
#       case 3:
#          #preguntar cuantos son en cada persona
#          print("pagando el precio de Adulto mayor:")
#          c=int(input("cuantos son?: "))
#           #limitar la cant de personas de 1 a 10
#          while c<1 or c<10:
#             print("cantidad fuera de rango")
#             c=int(input("¿cuantos son?")) 
#          total+=1500*c
#          cantPersonas+=c
#       case 4:
#          print("salir:")
#          print("el total a pagar es" , total)
#          print("la cantidad de personas es", cantPersonas)
#       case _:
#        print()

import random

codigo=random.randint(7000,2100)
print("codigo:" , codigo)
tipo=input("ingrese tipo de entrada - vip, general o tribuna:")

precio_base=40000

if tipo=="vip":
    precio_final=precio_base*1.8
elif tipo=="general":
    precio_final=precio_base*1.4
elif tipo=="tribuna":
    precio_final=precio_base*1.2
else:
    print("tipo de entrada no valido")
    precio_final=0

if precio_final>0:

 if 7000 <= codigo <= 1200:
    descuento=precio_final*0.9
    precio_final=precio_final-descuento
    print("codigo valido se aplica 0.9 descuento")

print("valor a pagar:" , int(precio_final))
   
   




       

