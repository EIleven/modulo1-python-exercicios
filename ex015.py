#Exercício Python 15: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
# e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
km = float(input('Quantos quilometros foram percorridos pelo carro? '))
d = int(input('Por quantos dias ele foi alugado? '))
p = (d * 60) + (km * 0.15)
print(f'O valor total do aluguel é de R${p:.2f}')
