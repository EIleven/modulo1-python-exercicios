from datetime import date
ano = int(input('Digite um ano para saber se ele é BISSEXTO ou digite 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:  # ATENÇÃO PARA O SÍMBOLO DE DIFERENTE (!=)
    print(f'O ano {ano} é bissexto')
else:
    print(f'O ano {ano} NÃO é bissexto')
