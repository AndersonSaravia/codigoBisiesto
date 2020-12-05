año=int(input("usuario, por favor ingrese un año\n"))

if (año%4==0 and año%100!=0):
    
    print("el año que usted ingresó es viciesto")
else:
    print("el año no es viciesto")