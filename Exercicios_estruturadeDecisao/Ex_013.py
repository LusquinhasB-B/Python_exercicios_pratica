'''Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.'''
t = "*"*50
print("Siga as intruções \nEscolha o número correpondente da semana!")
print(t)
print("1-   Domingo\n2-   Segunda \n3-   Terça \n4-   Quarta \n5-   Quinta \n6-   Sexta \n7-   Sábado") 



def dia_semana():
    dia = int(input("Insira o número: "))
    if dia == 1:
        print("Hoje é domingo! Bom começo de semana!")
    elif dia == 2:
        print("Hoje é segunda feira! Não compensa")
    elif dia == 3:
        print("Hoje é terça-Feira")
    elif dia == 4:
        print("Hojé é quarta-feira")
    elif dia == 5:
        print("Hoje é quinta-feira")
    elif dia == 6:
        print("Hoje é sexta-feira! SEXTOOOU")
    elif dia == 7:
        print("Hoje é sábado! Compensa sim")
    elif dia > 7 or dia < 1:
        print("Erro! número informado incorretamente!")
        dia_semana()

dia_semana()