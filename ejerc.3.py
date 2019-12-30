import math
print("Qué tal, hoy vamos a jugar !!")
print("Brindame el primer cateto")
x =int(input())
print("Brindame el segundo cateto ")
y = int(input())
hipotenusa = math.sqrt((x**2) + (y**2))
print( "La hipotenusa es " + str(hipotenusa))
