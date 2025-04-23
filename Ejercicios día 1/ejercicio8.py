#8. Clasificación de IMC

#Pide al usuario su peso (kg) y altura (m). Calcula su IMC (peso / altura²) y muestra:

#    "Bajo peso" si es menor a 18.5
#    "Normal" si está entre 18.5 y 24.9
#    "Sobrepeso" si está entre 25 y 29.9
#    "Obesidad" si es mayor o igual a 30

peso = float(input("Ingrese su peso en Kilogramos (kg): "))
altu = float(input("Ahora ingrese su altura en metros (m): "))

imc = peso/altu**2

if imc > 30:
    print("Obesidad")
elif imc >= 25 and imc <= 29.9:
    print("Sobrepeso")
elif imc >= 18.5 and imc <= 24.9:
    print("Normal")
else:
    print("Bajo peso")
    