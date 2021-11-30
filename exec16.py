import math

area_pintada = float(input('Informe a área a ser pintada em metros quadrados: '))
lata = float(80.00)

litros_necessarios = area_pintada / 3

quantidade_latas = math.ceil(litros_necessarios / 18)

print('É necessário {} latas para esse tamanho de área.' .format(quantidade_latas))