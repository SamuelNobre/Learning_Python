while True:
    num_01 = int(input("Digite um número maior que zero: "))

    if num_01 > 0:
        cont = 1
        while cont <= num_01:
            print(cont)
            cont += 1
    else:
        print("Por favor, digite um número maior que zero.")

    repetir = input("Gostaria de digitar outro número?")

    if repetir != 's':
        print("Obrigado por participar.")
        break

