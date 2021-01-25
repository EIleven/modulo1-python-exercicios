from math import hypot
co = float(input('Cateto oposto: '))
ca = float(input('Cateto adjacente: '))
print(f'O comprimento da hipotenusa para este triângulo retângulo será: {hypot(co, ca):.2f}')

# hi = (co ** 2 + ca ** 2) ** (1/2)