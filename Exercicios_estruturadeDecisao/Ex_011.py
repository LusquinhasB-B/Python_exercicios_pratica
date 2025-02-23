'''As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
    salários até R$ 280,00 (incluindo) : aumento de 20%
    salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
    salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
    salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
    o salário antes do reajuste;
    o percentual de aumento aplicado;
    o valor do aumento;
    o novo salário, após o aumento.'''
a = float(input('Insira o seu salário em reais(R$): '))
salario = float(f'{a:.2f}')

print(f"O salário atual informado é de: 'R${salario}'")
if salario <= 280:
    desconto20 = salario * (20/100)
    salario_novo20 = desconto20 + salario
    print(f"O valor do acréscimo é de 20%: 'R${desconto20}', seu salário após o reajuste é de: R${salario_novo20}")

elif salario > 280 and salario <= 700.00:
    desconto15 = salario * (15/100)
    salario_novo15 = desconto15 + salario
    print(f"O valor do acréscimo é de 15%: 'R${desconto15}', seu salário após o reajuste é de: R${salario_novo15}")
    
elif salario > 700 and salario <= 1500:
    desconto10 = salario * (10/100)#Desconto de 10% do salário
    salario_novo10 = desconto10 + salario
    print(f"O valor do acréscimo é de 10%: 'R${desconto10}', seu salário após o reajuste é de: R${salario_novo10}")

else:
    desconto05 = salario * (5/100)
    salario_novo05 = salario + desconto05
    print(f"O valor do acréscimo é de 5%: 'R${desconto05}', seu salário após o reajuste é de: R${salario_novo05}")





