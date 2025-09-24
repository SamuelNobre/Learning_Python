#Solicite 2 números para o usuário e informe qual dos 2 é maior.

num01 = int(input("Digite um número:"))
num02 = int(input("Digite outro número:"))

if num01 > num02:
    print(f"O número {num01} é maior que o {num02}")
elif num02 > num01:
    print(f"O número {num02} é maior que o {num01}")
else:
    print("Os números são iguais")