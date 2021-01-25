print('BEM VINDO AO CÁLCULO DE ÁREA E DE QUANTIDADE DE TINTA NECESSÁRIA PARA PINTÁ-LA. (1L PINTA 2M QUADRADOS)')

l = float(input('Largura da parede (metros): '))
a = float(input('Altura da parede (metros): '))
t = l * a
print(f'Área total = {t} metros quadrados')
print(f'Você precisará de {t/2} litros de tinta para pintar os {t} metros quadrados de área total.')
