nome = "Samuel porto"
altura = 1.75
peso = 115
imc = peso / (altura*altura)
#print(nome + " tem", altura, "m", "de altura", end="\n" + "Pesa " + str(peso) + "kg" + " e seu IMC é de " + str(imc))
linha_1 = f"{nome} tem {altura:.2f} de altura e pesa {peso} kg e seu imc é de {imc:.2f}"

print(linha_1)
