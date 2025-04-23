# 5. Calculadora de Propinas

#Pide al usuario el total de una cuenta. Luego pregunta qué porcentaje de propina quiere dejar (10, 15 o 20). Calcula y muestra el valor de la propina.

total = float(input("Ingrese el total de la cuenta: "))
porcprop = int(input("ingrese el porcentaje de propina que desea dejar (10, 15 o 20): "))

prop = porcprop * total / 100
print("El valor de la propina es: ", prop)