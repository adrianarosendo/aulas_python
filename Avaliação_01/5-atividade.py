

numero = input("Insira um número: ")
soma_total= 0

for i in range(0, len(numero)):
    soma_total = int(numero[i]) + soma_total

print("Soma dos algarismo é igual a:", soma_total)
