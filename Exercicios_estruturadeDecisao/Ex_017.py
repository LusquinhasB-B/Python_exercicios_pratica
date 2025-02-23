'''Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto.'''
n = int(input("Informe o ano: "))
if (n % 400) == 0 or n % 4 == 0 and n % 100 != 0:
    print("Ano é bissexto!")
else:
    print("Ano não é bissexto!")



