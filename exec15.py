valor_hora = float(input('Quanto você ganha por hora? '))
horas_mes = float(input('Quantas horas você trabalhou no mês? '))

a_salario_bruto = valor_hora * horas_mes

b_inss = a_salario_bruto * 0.08

c_sindicato = a_salario_bruto * 0.05

imposto_de_renda = a_salario_bruto * 0.11

descontos = b_inss + c_sindicato + imposto_de_renda

d_salario_liquido = a_salario_bruto - descontos

print('+ Salário Bruto : R$ ', a_salario_bruto)
print('- IR (11%) : R$ ', imposto_de_renda)
print('- INSS (8%) : R$ ', b_inss)
print('- Sindicato (5%) : R$ ', c_sindicato)
print('= Salário Líquido : R$ ', d_salario_liquido)
