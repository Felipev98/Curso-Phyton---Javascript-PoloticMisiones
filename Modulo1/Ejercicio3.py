#Escribe un programa en Phyton que acepte una cadena de caracteres y cuente el tamaño de la cadena y cuantas veces aparece la letra A(mayuscula) y (minuscula)

caracteres = input('Escriba una palabra: ')
contando = caracteres.lower()
contandoA = contando.count('a')
print('El número de veces que aparece la letra "A" es: ',contandoA)