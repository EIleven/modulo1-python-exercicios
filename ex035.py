print('\033[30;42m-=-\033[m' * 17)
print('\033[0;30;41m***** BEM VINDO(a) A CONSTRUÇÃO DE TRIÂNGULOS *****\033[m')
print('\033[30;42m-=-\033[m' * 17)
a = float(input('Comprimento da primeira reta: '))
b = float(input('Comprimento da segunda reta: '))
c = float(input('Comprimento da terceira reta: '))
# Para construir um triângulo é necessário que a medida de qualquer um dos lados seja menor que
# a soma das medidas dos outros dois e maior que o valor absoluto da diferença entre essas medidas.
if b - c < a < b + c and a - c < b < a + c and a - b < c < a + b:
# OU: a < b + c and b < a + c and c < a + b
    print(f'Os respectivos lados {a, b, c} FORMARÃO um triângulo')
else:
    print(f'Os lados {a, b, c} NÃO FORMARÃO um triângulo')
