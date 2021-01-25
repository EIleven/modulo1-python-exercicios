
n1 = float(input('Primeiro número: '))
n2 = float(input('Segundo número: '))
n3 = float(input('Terceiro número: '))
if n1 > n2 and n1 > n3:
    print(f'O número {n1} é o MAIOR entre os três')
if n2 > n1 and n2 > n3:
    print(f'O número {n2} é o MAIOR entre os três')
if n3 > n1 and n3 > n2:
    print(f'O número {n3} é o MAIOR entre os três')
if n1 < n2 and n1 < n3:
    print(f'O número {n1} é o MENOR entre os três')
if n2 < n1 and n2 < n3:
    print(f'O número {n2} é o MENOR entre os três')
if n3 < n1 and n3 < n2:
    print(f'O número {n3} é o MENOR entre os três')

print('******* RESOLUÇÃO *********')
a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))
# VERIFICANDO QUEM É MENOR:
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
# VERIFICANDO QUEM É O MAIOR:
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print(f'O menor valor digitado foi {menor}')
print(f'O maior valor digitado foi {maior}')
