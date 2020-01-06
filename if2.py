contra = "andres"
print("Ingresar contrasseña")
clave = input()
while clave != contra :
    print("Clave incorrecta")
    print("¿Desea volver a intentarlo? (S/N) :")
    OT_vez=input()
    if OT_vez.upper() == "N" :
        break
if clave == contra :
    print("ingreso correcto")
    print("End")