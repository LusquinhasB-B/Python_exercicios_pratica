'''Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;'''

def baskara():
    a = int(input("Informe o valor de 'a': ")) 
    if a == 0:
            print("A equação não é de segundo grau!")
            t = input("Programa encerrado! Deseja Reiniciá-lo? (S/N) ").lower()
            if t == "s":
                baskara()
            elif t == "n":
                print("ENCERRADO!")  
                 
    else:
        b = int(input("Informe o valor de 'b': "))
        c = int(input("Informe o valor de 'c': "))
        delta = (b**2) - 4*a*c
        if delta < 0:
            print("A equação não possui raizes reais! Programa encerrado")
            n = input("Deseja- reiniciá-lo? (S/N) ").lower()
            if n == 's':
                baskara()
            elif n == "n":
                 print("Programa encerrado! ")
        elif delta == 0:
            print("Com delta = 0 terá apenas uma raiz! ")
            x1 = (-b +(delta)) / (2 * a)
            print(f"A unica raiz corresponde a: '{x1:.1f}'")

        else:
            x1 = (-b +(delta)) / (2 * a)
            x2 = (-b -(delta)) / (2 * a)
            print(f"A raiz positiva corresponde a: '{x1:.1f}'")
            print(f"A raiz negativa corresponde a: '{x2:.1f}'")

baskara()
    




