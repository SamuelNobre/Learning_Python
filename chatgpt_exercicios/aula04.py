while True:
    sen_corr = "salame"

    tentativas = 1
    while tentativas < 3:
        senha = input("Digite sua senha: ")
        if senha.upper() == sen_corr:
            print("Seja bem vindo!")
            tentativas += 1
            
        else:
            print("Digite a senha correta")
            
