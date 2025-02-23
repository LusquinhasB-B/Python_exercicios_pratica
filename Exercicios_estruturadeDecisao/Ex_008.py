'''Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.'''

preco1 = float(input("Insira o valor do produto 1: "))
preco2 = float(input("Insira o valor do produto 2: "))
preco3 = float(input("Insira o valor do produto 3: "))

if preco1 < preco2 and preco1 < preco3:
    print(f"O produto mais barato é o produto número um com um valor de 'R${preco1:.2f}'") 
elif preco2 < preco1 and preco2 < preco3:
    print(f"O produto mais barato é o produto número dois com um valor de 'R${preco2:.2f}'")
elif preco3 < preco2 and preco3 < preco1:
    print(f"O produto mais barato é o produto número três com um valor de 'R${preco3:.2f}'")
else:
    print("Todos os precos são iguais")