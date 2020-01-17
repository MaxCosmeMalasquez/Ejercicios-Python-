indicador = False 
for var in range (1,6) :
    print("Ingresé un número")
    x =int(input())
    if x %2 == 0 : 
        indicador= True 
if indicador : 
    print(" introdujo Numero par")
else :
    print(" Introdujo algun Numero impar")