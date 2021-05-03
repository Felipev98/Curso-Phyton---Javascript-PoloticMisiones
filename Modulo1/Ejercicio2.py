#Escriba un programa en Phyton que acepte un número entero(n) y calcule el valor de n+ n*n + n*n*n
numero = int(input('Escriba un número: '))
resultado = numero+ (numero*numero) + (numero*numero*numero)
print('El resultado es: ',resultado)