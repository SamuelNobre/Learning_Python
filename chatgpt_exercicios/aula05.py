contador = 0
senha = "123"

while contador < 3:

    solicitar_senha = input("Digite sua senha: ")
    if solicitar_senha == senha:
        print("Seja bem vindo")
        break
    else:
        contador += 1
    
    if contador < 3:
        print("Senha incorreta, digite novamente.")
    else:
        print("Senha bloqueada, contacte seu admnistrador.")