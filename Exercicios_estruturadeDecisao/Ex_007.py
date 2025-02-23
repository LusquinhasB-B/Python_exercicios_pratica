'''Faça um Programa que leia três números e mostre o maior e o menor deles.'''
n1 = int(input("Insira um numero: "))
n2 = int(input("Insira outro numero: "))
n3 = int(input("Digite outro número: "))
 
#Verificar se o n1 é o maior número
if n1 > n2 and n1 > n3:
    print(f"{n1} é o maior número")
    if n2 > n3: 
        print(f"E o {n3} é menor número")
    else:
        print(f"E o {n2} é o menor número")
#Verificar se o n2 é o maior número
elif n2 > n1 and n2 > n3:
    print(f"{n2} é o maior número")
    if n3 > n1:
        print(f"E o {n1} é o menor número")
    else:
        print(f"E o {n3} é o menor número")

#Verificar se o n3 é o maior número
elif n3 > n1 and n3 > n2:
    print(f"{n3} é o maior número")
    if n2 > n1:
        print(f"E o {n1} é o menor número")
    else:
        print(f"E o {n2} é o menor número")

#Senão são todos iguais
else: 
    print("São todos iguais")