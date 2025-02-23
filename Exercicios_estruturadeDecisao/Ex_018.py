'''Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.'''


dia = int(input("Insira o dia do mês: "))
if dia > 0 and dia < 31:
    print("Dia valido")
    mes = int(input(f"Insira o mês do ano: {dia}/"))
    if mes > 0 and mes < 13:
        print("mês válido!")
        ano = int(input(f"Insira o ano: {dia}/{mes}/")) 
        if ano > 0:
            print("Ano válido")
            print(f"A data informada é: {dia}/{mes}/{ano}")
        else:
            print("Ano inválido")
    else:
        print("Mês inválido")
else:
    print("Dia invalido")

