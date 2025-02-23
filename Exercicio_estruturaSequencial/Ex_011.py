
# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# o produto do dobro do primeiro com metade do segundo .
# a soma do triplo do primeiro com o terceiro.
# o terceiro elevado ao cubo.
a = int(input("Digite um numero inteiro: "))
b = int(input("Digite outro numero inteiro: "))
c = float(input("Agora digite um numero real: "))

S1 =  (a*2)*(b/2)
S2 = (a*3) + c
S3 = c ** 3

print("{:.2f}\n{:.2f}\n {:.2f}".format(S1
, S2, S3))
