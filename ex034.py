print('\033[7;31m***** PROGRAMA PARA SABER O VALOR DO AUMENTO (10% OU 15%?)\033[m')
s = float(input('Digite o salário: R$'))
if s > 1250:
    print(f'Quem ganhava R${s:.2f} irá ganhar R$\033[32m{s * 0.10 + s:.2f}\033[m')
else:
    print(f'Quem ganhava R${s:.2f} irá ganhar R$\033[32m{s * 0.15 + s:.2f}\033[m')
