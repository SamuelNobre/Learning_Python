"""
Soma acumulada
Peça números ao usuário e vá somando.
O programa deve parar quando o usuário digitar 0, e então mostrar a soma total.
"""

soma = 0

while True:
    solicitar_num = int(input("Digite seu número: "))
    if solicitar_num == 0:
        print(f"O resultado é: {soma}")
        break
    soma += solicitar_num   
    