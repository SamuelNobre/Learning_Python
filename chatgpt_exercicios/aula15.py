#Tabuada
""" Minha primeira resolução
tab = int(input("Qual tabuada você gostaria de ver: "))

print(tab*1)
print(tab*2)
print(tab*3)
print(tab*4)
print(tab*5)
print(tab*6)
print(tab*7)
print(tab*8)
print(tab*9)
print(tab*10)
"""

#Resolução após correção

tab = int(input("Qual tabuada você gostaria de ver: "))

for i in range(1,11):
    print(f"{tab} x {i} = {tab*i}")