'''Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.'''
n = int(input("Insira qualquer numero nteiro: "))

if n > 0:
    print(f"{n} é um número positivo!")
elif n < 0:
    print(f"{n} é um número negativo")
else:
    print("{} é igual a zero (0)".format(n))
