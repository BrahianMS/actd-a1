# 2. Verificar si un número está en una lista

#    Crea una lista con 5 números.
#    Pide un número al usuario y verifica si está en la lista usando in.

lista = [2, 4, 7, 8, 11]
num = int(input("ingrese un número para verificar si está en la lista: "))

if num in lista:
    print("se encuentra en la lista")
else:
    print("no se encuentra en la lista")