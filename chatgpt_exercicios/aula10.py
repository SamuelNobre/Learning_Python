"""
Validação de idade
Peça a idade do usuário. Enquanto ele digitar algo que não seja um número positivo inteiro, 
repita a pergunta.
"""
while True:
    try:
        pedir_idade = int(input("Digite sua idade: "))
        if pedir_idade > 0:
            print(f"Sua idade é: {pedir_idade}")
            break
    except:
        print("Digite um valor correto.")