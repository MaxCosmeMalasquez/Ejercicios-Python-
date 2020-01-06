acumulador =  0 
for var in range(1,6):
    print("Ingresé un número")
    x = int(input())
    if x %2 == 0 : 
        acumulador = acumulador + x 
print("La suma de los numeros pares es " , acumulador )