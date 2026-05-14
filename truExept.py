# while True:
#  try:
#   num=int(input("ingrese in numero: "))
#   break
#  except:
#   print("solo debe ingresar numeros enteros: ")



# op=0
# total=0
# while op!=4:
#   try:
#     print("1._pc $500.000")
#     print("2._LGTV SS $450.000")
#     print("3._Microondas Mademsa $100.000")
#     print("4.- salir")
#     print("seleccione una opcion")
#     op=int(input())
#   except ValueError as e:
#     print("error", e)
#     print("solo se aceptan numeros enteros")
#     match op:
#         case 1:
#             print("el total a pagar es" , 500000*1.19)
#             total+=500000-1.19
#         case 2:
#             print("el total a pagar es" , 450000*1.19)
#             total+=450000-1.19
#         case 3:
#             print("el total a pagar es" , 100000*1.19) 
#             total+=100000-1.19
#         case 4:
#             print("saliendo")
#             print("el total a pagar es" , total)
#         case _:
#             print("opcion invalida")



# while True:
#     try:
#         num=int(input("Ingrese un numero: "))
        
#     except ValueError as er:
#         print("Error", er)
#         print("Solo debe ingresar numeros enteros")
#     else:
#         print("Numero ingresado correctamente")
#         break

       
# op=0
# total=0
# while op!=4:

# while True:
#     try:
#         notas=int(input("Ingrese la cant de notas: "))
#         break
#     except:
#         print("solo numeros enteros")

# suma=0
# for i in range(notas):
#     while True:
#         try:
#          n=float(input(f"Ingrese la nota {i+1}: "))
#          break
#         except: ValueError
#         print("solo numeros enteros")
#         suma=suma+n
#             # suma+=n
#     prom=suma/notas
#     print("El promedio es",round(prom,1) )

#     if prom>=4:
#             print("Alumno aprobado")
#     else:
#             print("Alumno reprobado")

#     #sumatoria


#     num=int(input("Ingrese un numero: "))
#     total=0
#     for i in range(num):
#         total=total+i+1
#     print(f"El resultado es {total}")


# correjir
# while True:
#    try:
#     notas=int(input("Ingrese la cant de notas: "))
#     suma=0
#     for i in range(notas):
#         n=float(input(f"Ingrese la nota {i+1}: "))
#         break
#    except: ValueError
#    suma=suma+n
#     # suma+=n
#    prom=suma/notas
#    print("El promedio es",round(prom,1) )

#    if prom>=4:
#     print("Alumno aprobado")
#    else:
#     print("Alumno reprobado")

#     #sumatoria


#     num=int(input("Ingrese un numero: "))
#     total=0
#     for i in range(num):
#         total=total+i+1
#     print(f"El resultado es {total}")

# totalingresos=0

# pasajes=int(input("cuantos pasajes deseas vender "))
# for i in range(pasajes):
#     try:
#         precio=int(input(f"ingrese el precio de los pasajes {i+1}: "))
#         totalingresos+=precio
#     except:
#         print("error necesitas proporcionar un valor numerico valido")
#         break
# print("el total de ingresos por la venta de pasajes es:", totalingresos)

saldo=100000
op=0
while True:
   try:
    op=int(input( '''
                        --- CAJERO ---
                        1.- ver saldo
                        2.- retirar
                        3.- depositar
                        4.- salir
                        '''))
   except ValueError:
     print("ese no es un numero. intenta de nuevo")

   if op==1:
        print("tu saldo es", saldo)
        
   elif op==2:
    monto = int(input("cunto quieres retirar "))
    
    if monto > saldo:
      print("no tienes suficiente dinero")
    elif monto % 5000!=0:
      print("solo puedes retirar multiplos de 5000")
    else:
      saldo-=monto
      print("listo. saldo ahora:", saldo)

   elif op==3:
    monto = int(input("cuanto quieres depositar "))
    if monto % 5000 !=0:
      print("solo puedes depositar multiplos de 5000")
    else:
      saldo+=monto
      print("listo. Saldo ahora:", saldo)
    
   elif op == 4:
     print("saliendo")
     break
   else:
     print("opcion invalida")



