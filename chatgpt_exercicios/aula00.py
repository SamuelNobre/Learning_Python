from datetime import datetime

nome = input("Digite seu nome:")
idade = int(input("Qual sua idade? "))
ano_atual = datetime.now().year
idade_centenario = (100 - idade) + ano_atual
print(f"{nome}, você vai completar 100 anos em {idade_centenario}.")

#print("Sua idade é:", idade)
#print("Olá, seja bem vindo", nome,"!")