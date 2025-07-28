"""
Solicitar 2 valores para o usuário e um operador, realizar o cálculo conforme 
as informações solicitadas
"""
#Versão 01 do código
"""while True:
    num01 = int(input("Por favor insira um valor: "))
    num02 = int(input("Por favor insira outro valor: "))
    operador = input("Digite o operador do seu cálculo: ")
    soma = num01 + num02 )
    sub = num01 - num02  | Podemos calcular isso dentro do if, não precisamos fazar todos os cálculos
    mult = num01 * num02 | antes de exibir o resultado para o usuário.
    divs = num01 / num02 )

    if operador == "+":
        print(f"Seu cálculo foi uma soma e o valor é:{soma}")
    elif operador == "-":
        print(f"Seu cálculo foi uma subtração e o valor é: {sub}")
    elif operador == "*":
        print(f"Seu cálculo foi uma multiplicação e o valor é: {mult}")
    elif operador == "/": # Podemos evitar o erro de divisão por 0
        print(f"Seu cálculo foi uma divisão e o valor é: {divs}")

    # Podemos evitar o erro de o usuário selecionar um operador diferente dos propostos com um else.
    break
"""
#Versão após correção
while True:
    num01 = int(input("Por favor insira um valor: "))
    num02 = int(input("Por favor insira outro valor: "))
    operador = input("Digite o operador do seu cálculo: ")

    if operador == "+":
        print(f"Seu cálculo foi uma soma e o valor é: {num01+num02}")
    elif operador == "-":
        print(f"Seu cálculo foi uma subtração e o valor é: {num01-num02}")
    elif operador == "*":
        print(f"Seu cálculo foi uma multiplicação e o valor é: {num01*num02}")
    elif operador == "/":
        if num02 != 0:
            print(f"Seu cálculo foi uma divisão e o valor é: {num01/num02}")
        else:
            print("Erro: Divisão por zero não permitida")
    else:
        print("Operador inválido, Tente novamente.")
    break