#7. Mayor de Dos Números

#Pide dos números al usuario. Imprime cuál es el mayor. Si son iguales, indícalo.

num1 = float(input("Ingrese un número: "))
num2 = float(input("Ingrese otro número: "))

if num1 > num2:
    print(num1, "es mayor")
elif num1 < num2:
    print(num2, "es mayor")
else:
    print("ambos números son iguales")