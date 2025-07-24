"""
Senha correta
Peça ao usuário uma senha. Se for diferente de "1234", peça novamente até ele acertar.
Quando acertar, exiba: "Acesso permitido".

"""

senha_correta = "1234"
tentativas = 0

while tentativas < 5:
    solicitar_senha = input("Olá, digite sua senha: ")
    if solicitar_senha == senha_correta:
        print("Seja bem vindo!")
        break
    else:
        print("Senha incorreta, digite de novo")
        tentativas += 1
    
if tentativas == 5:
    print("Número de tentativas esgotadas, por gentileza contacte o seu admnistrador.")
