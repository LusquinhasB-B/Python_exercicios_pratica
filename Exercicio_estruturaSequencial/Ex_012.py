'''
Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58
'''
h = float(input("Digite a altura correspondente: "))

peso_ideal = (72.76*h) - 58

print("O peso ideal com base na altura inserida é de: {:.2f}Kg".format(peso_ideal))