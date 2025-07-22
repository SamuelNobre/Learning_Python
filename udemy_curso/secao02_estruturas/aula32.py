"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
num_01 = input("Digite um número inteiro: ")

try:
    conversor = int(num_01)
    if conversor % 2 == 0:
        print("isso é um número par.")
    elif conversor % 2 != 0:
        print("Isso é um número ímpar.")
except:
    print("Isso não é um número inteiro.")


"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

nome = input("Olá, qual o seu nome? ")
hora = int(input("Que horas são? "))

if hora >= 0 and hora <= 11:
    print(f"Olá {nome}, Bom dia! São {hora} horas.")
elif hora >= 12 and hora <= 17:
    print(f"Olá {nome}, Boa tarde! São {hora} horas.")
elif hora >= 18 and hora <= 23:
    print(f"Olá {nome}, Boa noite! São {hora} horas.")
else:
    print(f"Por gentileza {nome}, digite um horário correto.")



"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome = input("Olá, qual seu nome? ")
tamanho = len(nome)

if tamanho <= 4:
    print(f"Olá {nome}, seu nome é curto.")
elif 5 <= tamanho <= 6:
    print(f"Olá {nome}, seu nome é normal.")
elif tamanho > 6:
    print(f"Olá {nome}, seu nome é muito grande.")
