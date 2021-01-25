from math import sin, cos, tan, radians
print('BEM VINDO AO PROGRAMA CÁLCULO DE SENO COSSENO E TANGENTE DE QUALQUER ÂNGULO, FEITO POR BRENO CÉSAR')
angulo = float(input('Digite o ângulo para saber seu seno, cosseno e tangente: '))
print(f'O SENO do ângulo de {angulo} graus é igual a {sin(radians(angulo)):.2f}')
print(f'O COSSENO é igual a {cos(radians(angulo)):.2f}')
print(f'Sua TANGENTE é igual a {tan(radians(angulo)):.2f}')
