#Problemática
"""
João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. 
"""
#Solução
"""João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas."""

#Leitura de dados
peso_peixes = float(input("Informe o valor do peso em Kilos(Kg): "))
diferenca = peso_peixes - 50
multa = diferenca * 4
print("#"+60*"*"+"#")
#calculo sobre excesso dos peixes
if peso_peixes > 50:
    print("O peso informado está acima do permitido")
    print(60*"*")
    print("Com base no peso inserido de '{:.2f}Kg'\nO valor da multa a ser paga é de 'R${:.2f}'".format(peso_peixes, multa))
else:
    print("O peso informado está dentro dos limites! Nenhuma multa a ser paga!")


