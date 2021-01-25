nome = str(input('Digite seu nome completo: ')).strip()
print(f'Nome com todas as letras maiúsculas: {nome.upper()}')
print(f'Nome com todas as letras minúsculas: {nome.lower()}')
n = nome.replace(' ', '')
print(f'Quantidade de letras com espaços: {len(nome)}')
print(f'Quantidade total de letras (sem espaços): {len(n)}')
n2 = nome.split()
print(f'O primeiro nome é {n2[0]} e possui {len(n2[0])} letras')


#Resolução: Lembrando que a função .strip() vai garantir que a entrada de um nome não inclua possíveis espaços digitados
#pela pessoa antes ou depois de digitar o nome

# Para contar a quantidade de letras, também podemos usar o seguinte modelo: len(nome) - nome.count(' ')
# E, para saber a quantidadede letras no primeiro nome podemos fazer do seguinte modo: nome.find(' ')
#