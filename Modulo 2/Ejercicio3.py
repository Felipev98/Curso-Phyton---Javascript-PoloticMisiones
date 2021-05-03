#Escribe un programa en Python que reciba 5 números enteros del usuario y los guarde en una lista.
#Luego recorrer la lista y mostrar los números por pantalla. 
i = 0
numeros = []

while i != 5:
    numerosEnteros = int(input('Escriba un número entero: '))
    guardarNumero = numeros.append(numerosEnteros)
    i+=1
for i in numeros:
    print(i)