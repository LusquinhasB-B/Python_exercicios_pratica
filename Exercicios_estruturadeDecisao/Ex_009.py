
#Faça um Programa que leia três números e mostre-os em ordem decrescente.
while True:
    n1 = int(input("Digite o 1ºnúmero: "))
    n2 = int(input("Digite o 2ºnúmero: "))
    n3 = int(input("Digite o 3ºnúmero: "))

    if n1 > n2 > n3:
        print(f"A ordem correspondente é: {n1}, {n2}, {n3}")
        if n3 > n2:
            print(f"A ordem correspondente é: {n1}, {n3},{n2}")
        elif n3 == n2:
            print(f"A ordem correspondente é: {n1}, {n3} ,{n2} sendo {n3} e {n2} iguais" )
        
    elif n2 > n1 > n3:
        print(f"A ordem correspondente é: {n2},{n1},{n3}")
        if n3 > n1:
            print(f"A ordem correspondente é: {n2}, {n3}, {n1}")
        elif n3 == n1:
            print(f"A ordem correspondente é: {n2}, {n3}, {n1} sendo {n3} e {n1} iguais")
        
    elif n3 > n1 > n2:
        print(f"A ordem correspondente é: {n3}, {n1}, {n2}")
        if n1 < n2:
            print(f"A ordem corresponte é: {n3}, {n2}, {n1}")
        if n1 == n2:
            print(f"A ordem corresponte é: {n3}, {n2}, {n1} sendo {n1} e {n2} iguais")

    else:
        print("São todos iguais, sem ordem definida")    

