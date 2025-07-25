"""
Transforte o resultado da variável nome em *n*o*m*e*

"""

#       012345678910
# nome = 'Samuel Porto'  # Iteráveis
#      1110987654321


nome = 'Samuel Porto'  # Iteráveis

indice = 0
novo_nome = ''
while indice < len(nome):
    letra = nome[indice]
    novo_nome += f'*{letra}'
    indice += 1

novo_nome += '*'
print(novo_nome)