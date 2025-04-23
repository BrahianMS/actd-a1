# 9. Año Bisiesto

# Pide un año al usuario. Determina si es bisiesto (es divisible entre 4 y no entre 100, excepto si también es divisible entre 400).

a = int(input("Ingrese un año: "))

if a % 100 != 0:
    if a % 4 == 0:
        print("es bisiesto")
    else:
        print("no es bisiesto")
elif a % 100 == 0 and a % 400 == 0:
    print("es bisiesto")
else:
    print("no es bisiesto")