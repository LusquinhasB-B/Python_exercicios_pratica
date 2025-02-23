'''Faça um Programa que peça dois números e imprima o maior deles.'''
n1 = int(input("Insira um número: "))
n2 = int(input("Insira outro numero: "))

if n1 > n2:
    print(f"O numero {n1} é maior que o numero {n2}")
elif n2 > n1:
    print(f"O numero {n2} é maior que o número {n1}")
else:
    print("Ambos são iguais")
