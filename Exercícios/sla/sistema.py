def cadastro_senha():
    senha = int(input("informe a senha: "))
    confirma_senha = int(input("Confirme a senha: "))
    if confirma_senha == senha:
        print("Senha cadastrada com sucesso!")
    else:
        print("Senha incorreta, informe corretamente!")
        return cadastro_senha()
    
def cadastro_nome():
    nome = str(input("Informe o seu nome: "))   
    confirma_nome = input("Deseja alterar o nome? S/N ")
    if confirma_nome == "N":
        print("Nome não alterado!")
        pass
    elif confirma_nome == "S":
        print("teste")
        return cadastro_nome()
    
cadastro_senha()