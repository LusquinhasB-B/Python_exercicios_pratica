"""Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:"""

# Jornada mensal: 220 horas;
salario_hora = float(input("Informe o seu salário hora(R$)\nEx:6.26: "))
horas_trabalhadas_mensal = int(input("Informe as horas trablhas durantes o mês\nEx: 220 horas: "))

#Salário bruto calculado
salario_hora_mensal = salario_hora * horas_trabalhadas_mensal
#Descontos do salário liquido
imposto_renda = salario_hora_mensal * (11/100)
inss = salario_hora_mensal * (8/100)
sindicato =  salario_hora_mensal * (5/100)

descontos = imposto_renda + inss + sindicato
#Valor do salário liquido apos os descontos
salario_liquido = salario_hora_mensal - descontos
#resultados
print(f"Seu salário bruto mensal, com base nos valores inseridos corresponde a: 'R${salario_hora_mensal:.2f}'! Sem a adicão de descostos!")
print(f"Os valores dos descontos correspondentes ao seu salário informado são:\n> Imposto de renda(11%): R${imposto_renda:.2f}\n> INSS(8%) R${inss:.2f} \n> Sindicato(5%): R${sindicato:.2f}")
print(f"O valor do salário líquido pós adicão de descontos é de: 'R${salario_liquido:.2f}'")



