#Criar um código onde imprima o indece do intem na lista e o item

"""nomes = ["Samuel", "Lionete", "Marcio"]

for indice, nome in enumerate(nomes, start=1):
    print(indice, nome)
"""
"""
Exercício
Exiba os índices da lista
0 Maria
1 Helena
2 Luiz
"""
lista = ['Maria', 'Helena', 'Luiz']
lista.append('João')


indices = range(len(lista))

for indice in indices:
    print(indice, lista[indice], type(lista[indice]))