"""
Média de notas
Peça ao usuário para digitar quantas notas ele quer informar.
Em seguida, use while para receber todas as notas e calcule a média ao final.
"""
#Versão inicial do código
"""
notas = int(input("Olá, quantas notas você irá informar?"))
contador = 0
soma = 0
while contador < notas:
    informar_notas = int(input("Nota: "))
    if contador < notas: # Não existia a necessidade de criar um if, pois o laço encerrava sozinho
        soma += informar_notas
        contador += 1
    if contador == notas:
        print(f"Média: {soma/notas}") # Tirei esse cálculo da média de dentro do print e fiz uma vari-
        break                           -ável para o código ficar mais limpo.
        

"""
#Versão após correção
   
notas = int(input("Olá, quantas notas você irá informar?"))
contador = 0
soma = 0
while contador < notas:
    informar_notas = int(input("Nota: "))
    soma += informar_notas
    contador += 1

media = soma/notas
print(f"Média: {media}")
