deuda=100000
op=0
while True:
    op=int(input( '''
                        --- MENU ---
                        1.- pago tarjeta de credito
                        2.- simulacion de compra
                        3.- salir
                        '''))
    print("deuda actual:", deuda)
 

    if op==1:
     try:
        pago=int(input("cuanto vas a pagar"))

        if pago<0:
          print("No puedes pagar un numero negativo")
        elif pago>deuda:
          print("Mo puedes pagar mas de los que debes")
        else:
          deuda-=pago
          print("Pago hecho, Ahora debes:", deuda)
     except:
       print("Eso no es un numero")
    
    
    elif op==2:
     try:
        compra=int(input("cuanto cuesta la compra"))

        if compra<0:
          print("No puedes comprar un valor negativo")
        else:
          deuda+=compra
          print("Compra hecha, Ahora debes:", deuda)
     except:
       print("Eso no es un numero")
    

    elif op==3:
      print("chao")
      break
    
    else:
     print("opcion invalida. Escribe 1, 2 o 3")
