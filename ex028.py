from random import randint
from time import sleep
print('-=-' * 20)
print('VOU PENSAR EM UM NÚMERO ENTRE 0 E 5. TENTE ADVINHAR...')
print('-=-' * 20)
ni = randint(0, 5)
n = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(2)
if n == ni:
    print(f'PARABÉNS, VOCÊ LEU MEUS CÓDIGOS, EU PENSEI NO {ni}! HARE KRISHNA!')
else:
    print(f'VOCÊ VACILOU! Eu pensei no número {ni} e não no {n}')
