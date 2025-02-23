'''Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
    Desconto do IR:
        Salário Bruto até 900 (inclusive) - isento
        Salário Bruto até 1500 (inclusive) - desconto de 5%
        Salário Bruto até 2500 (inclusive) - desconto de 10%
        Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.
        Salário Bruto: (5 * 220)        : R$ 1100,00
        (-) IR (5%)                     : R$   55,00  
        (-) INSS ( 10%)                 : R$  110,00
        FGTS (11%)                      : R$  121,00
        Total de descontos              : R$  165,00
        Salário Liquido                 : R$  935,00'''

t = "*"*50
print("Siga as intruções")
print(t)
a = float(input("Informe o valor recebido POR DIA de trabalho: "))
print(t)
b = float(input("Informe as horas MENSAIS trabalhadas: "))
print(t)
salario_bruto = float(f'{a*b:.2f}')
#Calculando o valor de desconto do FGTS com base no valor inserido
desconto_FGTS = salario_bruto * 11/100
desconto_INSS = salario_bruto * 10/100
#Salário após o desconto do FGTS

print(f"Salário bruto               : R${salario_bruto}")

#Calculo do imposto de renda com base no salário bruto
if salario_bruto <= 900:
    print("isento do IR (Imposto de renda)")   

elif salario_bruto <= 1500:
    desconto05 = salario_bruto * (5/100)
    total_descontos05 = desconto_INSS + desconto05
    salário_líquido05 = salario_bruto - total_descontos05 
    print(f"(-) IR (5%)                 : R${desconto05}")
    print(f"(-) INSS (10%)              : R${desconto05}")
    print(f"FGTS (11%)                  : R${desconto_FGTS:.2f}")
    print(f"Total de descontos          : R${total_descontos05}")
    print(f"Salário líquido             : R${salário_líquido05}")
  
elif salario_bruto <= 2500:
    desconto10 = salario_bruto * (10/100)
    total_descontos10 = desconto_INSS + desconto10
    salário_líquido10 = salario_bruto - total_descontos10
    print(f"(-) IR (10%)                : R${desconto10}")
    print(f"(-) INSS (10%)              : R${desconto10}")
    print(f"FGTS (11%)                  : R${desconto_FGTS:.2f}")
    print(f"Total de descontos          : R${total_descontos10}")
    print(f"Salário líquido             : R${salário_líquido10}")

else: 
    desconto20 = salario_bruto * (20/100)
    total_descontos20 = desconto_INSS + desconto20
    salário_líquido20 = salario_bruto - total_descontos20
    print(f"(-) IR (20%)                : R${desconto20}")  
    print(f"(-) INSS (10%)              : R${desconto20}")
    print(f"FGTS (11%)                  : R${desconto_FGTS:.2f}")
    print(f"Total de descontos          : R${total_descontos20}")
    print(f"Salário líquido             : R${salário_líquido20}")





