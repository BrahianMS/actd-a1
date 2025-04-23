# 4. Contraseña Correcta

#Pide una contraseña al usuario. Si coincide con "python123", imprime "Acceso concedido", de lo contrario, "Contraseña incorrecta".

contra = str(input("Ingrese la contraseña: "))
if contra == "python123":
    print("Acceso concedido")
else:
    print("Contraseña incorrecta")