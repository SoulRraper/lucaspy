# while True:
#  try:
#   num=int(input("ingrese in numero: "))
#   break
#  except:
#   print("solo debe ingresar numeros enteros: ")



op=0
total=0
while op!=4:
  try:
    print("1._pc $500.000")
    print("2._LGTV SS $450.000")
    print("3._Microondas Mademsa $100.000")
    print("4.- salir")
    print("seleccione una opcion")
    op=int(input())
  except ValueError as e:
    print("error", e)
    print("solo se aceptan numeros enteros")
    match op:
        case 1:
            print("el total a pagar es" , 500000*1.19)
            total+=500000-1.19
        case 2:
            print("el total a pagar es" , 450000*1.19)
            total+=450000-1.19
        case 3:
            print("el total a pagar es" , 100000*1.19) 
            total+=100000-1.19
        case 4:
            print("saliendo")
            print("el total a pagar es" , total)
        case _:
            print("opcion invalida")


# while True:
#  try:
#   num=int(input("ingrese in numero: "))
 
#  except ValueError as er:
#   print("solo debe ingresar numeros enteros: ")
#   break

       
# op=0
# total=0
# while op!=4:


try:
    notas=int(input("Ingrese la cant de notas: "))
    suma=0
    for i in range(notas):
        n=float(input(f"Ingrese la nota {i+1}: "))
        suma=suma+n
        # suma+=n
    prom=suma/notas
    print("El promedio es",round(prom,1) )
except:
    if prom>=4:
        print("Alumno aprobado")
    else:
        print("Alumno reprobado")

    #sumatoria


    num=int(input("Ingrese un numero: "))
    total=0
    for i in range(num):
        total=total+i+1
    print(f"El resultado es {total}")
