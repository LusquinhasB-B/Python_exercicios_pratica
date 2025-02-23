'''Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
  Média de Aproveitamento  Conceito
  Entre 9.0 e 10.0        A
  Entre 7.5 e 9.0         B
  Entre 6.0 e 7.5         C
  Entre 4.0 e 6.0         D
  Entre 4.0 e zero        E
O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.'''

nota1 = float(input("Insira a sua 1º nota parcial: "))
nota2 = float(input("Insira sua 2º nota parcial: "))
media = (nota1 + nota2) / 2

print(f"A média do aluno é de '{media:.1f}.'")
if media <= 4.0 and media >= 0:
    print("Conceito:        E") 
    print("Situação:        REPROVADO!")
elif media < 6.0 and media >= 4.0:
    print("Conceito:        D") 
    print("Situação:        REPROVADO!")
elif media < 7.5 and media >= 6.0:
    print("Conceito:        C") 
    print("Situação:        APROVADO!")
elif media < 9.0 and media >= 7.5:
    print("Conceito:        B") 
    print("Situação:        APROVADO!")
elif media <= 10.0 and media >= 9.0:
    print("Conceito:        A") 
    print("Situação:        APROVADO!")



