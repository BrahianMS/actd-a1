# 6. Adivina el Número

#Fija un número secreto (por ejemplo, 7). Pide al usuario que lo adivine. Di si su número es mayor, menor o igual al número secreto.

numsec == 11
num = int(input("Intente adivinar el número secreto, ingrese un número del 1 al 20: "))

if num > numsec:
    print("Su número es mayor al número secreto")
elif num < numsec:
    print("Su número es menor al número secreto")
else:
    print("Adivinaste el número secreto")