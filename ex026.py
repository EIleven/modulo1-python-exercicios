frase = str(input('Digite uma frase: ')).strip().upper()
print(f'A letra "A" aparece {frase.count("A")} vezes')
print(f'A letra "A" aparece pela primeira vez em {frase.find("A")+1}')
print(f'A última letra "A" apareceu na posição {frase.rfind("A")+1} ')
