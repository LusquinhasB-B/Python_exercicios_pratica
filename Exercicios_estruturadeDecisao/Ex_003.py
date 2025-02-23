'''Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.'''
s = input("Digite 'F' se for mulher ou digite 'M' se for homem: ")

if s.lower() == "m":
    print("Masculino")
elif s.lower() == "f":
    print("Feminino")
elif s  != "M" or s != "F":
    print("Sexo inválido")