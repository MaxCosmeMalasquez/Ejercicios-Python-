print("¿Cuántas monedas tienes?")
print(" De 1$")
x = int(input())
one = x
print("De 2$ ")
y = int(input())
two = 2 * y
print("De 50 centavos")
z = int(input())
fifty= z*50
print("De 20 centavos")
w = int(input())
twenty = w  *20
print("De 10 centavos")
s = int(input())
ten = s*10
euros = (one+ two)
centavos = (fifty + twenty + ten )
print("Tengo " + str(x) + " monedas de 1$" )
print("Tengo " + str(y)+ " monedas de 2 $")
print("Tengo " + str(z) + " monedas de 50 centavos")
print("Tengo " + str(w)+ " monedas de 20 centavos")
print("Tengo " + str(s) + " monedas de 10 centavos")
print("Es así , que tengo " + str(euros) +  " $ y " + str(centavos) + " centavos" )

