#Peça um número ao usuário e diga se o mesmo é par ou impar.

num = int(input("Digite um número: "))
resto = num % 2

if resto == 0:
    print(f"O número: {num} é par.")
elif resto != 0:
    print(f"O número: {num} é ímpar.")