#Escriba un programa Phyton que acepte el radio de un círculo del usuario y calcule el área

radio  = float(input('Escriba su radio: '))
pi = 3.14159
areaCirculo = round((radio**2) * pi,2)
print(f'El área del circulo es: {areaCirculo}cm')