from datetime import datetime

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
ano_atual = datetime.now().year
idade_centenario = (100-idade)+ano_atual

#Primeiro código

#menu = int(input(f"Olá {nome}, escolha uma das opções abaixo: \n 1 - Ver mensagem \n 2 - Calcular anos \n 3 - Sair \n"))

#contador = 0
#while contador < 3:

#    if menu == 1:
#        print(f"Seja bem vindo: {nome}")
#    if menu == 2:
#        print(f"O ano que você completará 100 anos será em: {idade_centenario}")
#    contador += 1

while True:
    menu = int(input(f"Olá {nome}, escolha uma opção abaixo\n"
                     "1 - Ver mensagem. \n" \
                     "2 - Calcular ano em que você completa 100 anos \n" \
                     "3 - Sair. \n" \
                     "Opção: "))
    if menu == 1:
        print(f"Olá, seja bem vindo!")
    elif menu == 2:
        print(f"O Ano que você completará 100 anos será em: {idade_centenario}")
    elif menu == 3:
        print("Obrigado por acessar, encerrando sistema.")
        break
    else:
        print(f"Por gentileza {nome}, escolha uma opção válida.")