# 5. ¿Está en la lista de invitados?

#    Crea una lista con algunos nombres (por ejemplo: "Ana", "Luis", "Sofía").
#    Pide al usuario su nombre.
#    Usa if para decir si está en la lista de invitados o no.

lista = ["Ana", "Sofía", "Luis", "Pedro", "Jaime", "Oscar", "María", "John", "Carlos"]
nom = str(input("Ingrese su nombre: "))
if nom in lista:
    print("Está en la lista")
else:
    print("No está en la lista")