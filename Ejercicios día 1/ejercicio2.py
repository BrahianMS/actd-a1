# 2. Número Positivo o Negativo

#Pide un número al usuario. Di si es positivo, negativo o si es cero.

numero = float(input("ingrese un número: "))
if numero > 0:
    print("Es positivo")
elif numero < 0:
    print("Es negativo")
else:
    print("Es cero")
