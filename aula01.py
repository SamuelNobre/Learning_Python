from datetime import datetime

nome = input("Digite seu nome: ")
ano_atual = datetime.now().year
idade = int(input("Digite sua idade: "))
idade_18 = (18-idade)+ano_atual

if idade < 12: 
    print(f"{nome}, você é muito jovem para utilizar o sistema.")
    
elif 12 <= idade <= 17: 
    print(f"{nome}, você pode utilizar o sistema com autorização dos responsáveis.")
    
else : 
    print(f"{nome}, você poderá acessar o sistema.")
    
if idade < 18: 
    print(f"Olá {nome}, você irá completar 18 anos em: {idade_18}")

elif idade > 18: 
    print(f"Olá {nome}, você completou 18 anos em: {idade_18}")
