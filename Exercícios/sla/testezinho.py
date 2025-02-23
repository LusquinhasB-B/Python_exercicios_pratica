import sistema as sist
lista_senha = []
u = "*"*50
print("--- Olá seja bem-vindo ao teste do luquinhas")        
print(u)
print("Vamos iniciar o nosso cadastro!")

sist.cadastro_senha()
print(u)

print("O que deseja fazer?")
confirma = input("1º - Saber o nome cadastrado.\n2º - Saber o salario a senha cadastrado.\n3º - Sair.\nResposta:")
while True:
    if confirma == "1":
        print("o ")