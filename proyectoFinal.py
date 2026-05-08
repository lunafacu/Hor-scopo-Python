import os
import libreria1

os.system('cls')
print(libreria1.menuPrincipal)
opc=input("Ingrese una opción: ")
if opc.isnumeric():
    opc=int(opc)
while (opc!=0):
    if opc==1:
        libreria1.opc1()
    elif opc==2:
        libreria1.opc2()
    else:
        print("Ingrese una opción correcta.")
        os.system('pause')
        os.system('cls') 
    print(libreria1.menuPrincipal)
    opc=input("Ingrese una opción: ")
    if opc.isnumeric():
        opc=int(opc)
else:
    os.system('cls')
    print("="*40,"\n")
    print("¡Gracias por usar nuestro programa!\n".center(40))
    print("="*40,"\n")
    os.system('pause')
           