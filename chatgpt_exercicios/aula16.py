"""
Desafio:
Peça ao usuário um número inteiro N e mostre todos os números de 1 até N, mas:
Se o número for par, mostre junto a palavra "par".
Se o número for ímpar, mostre junto a palavra "ímpar".
"""

num01 = int(input("Digite um número inteiro: "))

for i in range(1, num01+1):
    if i % 2 == 0:
        print(f"{i} par")
    else:
        print(f"{i} ímpar")
        