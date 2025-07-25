"""
Número secreto
Gere um número secreto de 1 a 10 (pode definir fixo por enquanto).
Peça para o usuário tentar adivinhar, dando dicas de "maior" ou "menor".
Use um while até o acerto.
"""
sec = 3

while True:
    pedir_num = int(input("Tente acertar o número: "))
    
    if pedir_num < sec:
        print("Maior")
    elif pedir_num > sec:
        print("Menor")
    elif pedir_num == sec:
        print("Parabéns, você acertou!")
        break
    