from random import choice
a = input('Primeiro aluno: ')
b = input('Segundo aluno: ')
c = input('Terceiro aluno: ')
d = input('Quarto aluno: ')
n = choice([a, b, c, d])
print(f'O escolhido(a) foi {n}')
