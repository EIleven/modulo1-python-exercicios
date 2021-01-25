v = float(input('Digite a velocidade do carro: '))
if v > 80:
    m = (v - 80) * 7
    print(f'****** VOCÊ FOI MULTADO EM R${m:.2f}!! ******')
else:
    print('Siga em segurança.')
