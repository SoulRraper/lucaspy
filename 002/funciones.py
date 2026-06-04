#sin argumento y sin retorno
# def saludo():
#     print("hola lucash")
# n="nano"
# def chao():
#     print("nos vemos" , n)
# chao()

# def suma():
#  n1=int(input("ingrese un numero"))
#  n2=int(input("ingrese otro numero"))
#  print(f"el resultado es{n1+n2}")

# suma()

# con argumento y sin retorno
def saludame(name):
   print("Hola", name)

saludame("Ganon")

def restalos(n1, n2):
   print(f"El resultado de la sumresta es {n1-n2}")

restalos(88,9)


#sin argumento y con retorno

def multiplica():
    num1=8
    num2=23
    return num1*num2

vari=multiplica()*4
print(vari)

# con argumen y con retorno

# def restaCret(n1, n2):
#    return n1-n2

# print(restaCret(9, 3))

# crear una calculadora, para ejecutar 
# las operaciones basicas
# debe usar funciones con argumento y retorno

# def suma(n1, n2):
#    return n1+n2


# def resta(n1, n2):
#    return n1-n2


# def multiplicacion(n1, n2):
#    return n1*n2

# def division(n1, n2):
#    return n1/n2

# def calculadora():        
#     while True:
#         try:
#             print("1.- suma")
#             print("2.- resta")
#             print("3.- multiplicacion")
#             print("4.- division")
#             print("5- salir")
#             print("seleccione una opcion")
#             op=int(input())
#             match op:
#                 case 1:
#                     n1=int(input("Ingrese un numero: "))
#                     n2=int(input("ingrese otro numero: "))
#                     print("El resultado es", suma(n1,n2))
#                 case 2:
#                     n1=int(input("Ingrese un numero: "))
#                     n2=int(input("ingrese otro numero: "))
#                     print(resta(n1,n2))
#                 case 3:
#                     n1=int(input("Ingrese un numero: "))
#                     n2=int(input("ingrese otro numero: "))
#                     print(multiplicacion(n1,n2))
#                 case 4:
#                     n1=int(input("Ingrese un numero: "))
#                     n2=int(input("ingrese otro numero:"))
#                     print(division(n1,n2))
#                 case 5:
#                     print("saliendo")
#                     break
#                 case _:
#                     print("Numero invalido")
#         except Exception as e:
#             print("Error", e)
# calculadora()

#Crear un programa que calcule el IVA
#Y retorne el valor con IVA incluido
#Usar argumento y retorno

def C_IVA(precio):
    return precio *1.19

precio=float(input("Ingrese el precio neto: "))

print("Valor con IVA incluido", C_IVA(precio))
