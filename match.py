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


def tablademultiplicar ():
  num=int(input("ingre un num: "))
  for i in range(10):
    print(num , "*" , i+1, "=", num*(i+1))

def nombre():
  print("ingrese su nombre")
nombre=input
print("hola", nombre)

def pin():
  pin=int(input("crea un PIN de 4 digitos: "))

  if pin>1000 and pin <999:
     print("Pin creado")
  else:
     print("Pin invalido")

  if len(str()):
     print("Pin creado")
  else:
     print("Pin invalido")

   

def programas():        
     op=0
     while op!=4:
         print("1.- tabla de multiplicar")
         print("2.- nombre")
         print("3.- pin ")
         print("4.- salir ")         
         print("seleccione una opcion")
         op=int(input())
         match op:
             case 1:
              tablademultiplicar()
             case 2:
              nombre()
             case 3:
              pin()
             case 4:
              print("saliendo")
programas()




       

