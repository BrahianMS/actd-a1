# 1. Menor de tres números

#    Pide tres números al usuario.
#    Usa condicionales (if) para decir cuál es el más pequeño.

print("A continuación se le pediran tres números")
num1 = int(input("ingrese el primer número: "))
num2 = int(input("ingrese el segundo número: "))
num3 = int(input("ingrese el tercer número: "))

if num1 < num2 and num1 < num3:
    print(num1, "es el más pequeño")
elif num2 < num1 and num2 < num3:
    print(num2, "es el más pequeño")
elif num3 < num1 and num3 < num2:
    print(num3, "es el más pequeño")
    
