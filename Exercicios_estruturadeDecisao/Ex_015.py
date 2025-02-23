'''Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
Dicas:
Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
Triângulo Equilátero: três lados iguais;
Triângulo Isósceles: quaisquer dois lados iguais;
Triângulo Escaleno: três lados diferentes;'''
def triangulo():
    a = int(input("Informe o valor do 1º lado: "))
    b = int(input("Informe o valor do 2º lado: "))
    c = int(input("Informe o valor do 3º lado: "))
    if (b-c) < a < b + c and (a-c) < b < a + b and (a-b) < c < a + b: 
        print("Condição Verdadeira")
        if a == b != c or b == c != a or a == c != b:
            print("Triângulo Isósceles")
        elif a == b == c:
            print("Triângulo Equilátero")
        else:
            print("Triângulo Escaleno")
    else: 
        print("Condição Falsa\nInsira os valores novamente")
        triangulo()

triangulo()
        