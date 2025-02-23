'''
Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
Para homens: (72.7*h) - 58
Para mulheres: (62.1*h) - 44.7
'''
#Variaveis
altura = float(input("Digite a sua altura, em metros: "))

#Lógica
peso_ideal_masc = (72.7*altura) - 58
peso_ideal_femi = (62.1*altura) - 44.7

#Resultado
print("O peso ideal, caso seja do gênero masculino é de: {:.2f}Kg".format(peso_ideal_masc))
print("O peso ideal caso seja do gênero feminino é de: {:.2f}Kg".format(peso_ideal_femi))


