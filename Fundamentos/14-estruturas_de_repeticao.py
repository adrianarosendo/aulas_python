#Vai escrever no console todos os números em ordem decrescente do número digitado

numero = int(input("Digite um número: "))
contador = 0
while contador <= numero:
    print(numero - contador)
    contador = contador + 1

#Vai escrever no console todos os itens da lista
lista = ["banana", "maça", "melancia", "caju"]

for item in (lista):
    print(item)

#Vai escrever no console todos os itens da lista inciados com a letra "m"
for item in (lista):
    if item[0] == "m":
        print(item)

#Vai escrever no console a idade da Ana.
nomes = {"Ana": 12, "João": 21, "Letícia": 76, "Isaque": 12}

if "Ana" in nomes:
    print('Encontramos a idade da Ana, que é %d no dicionário' %nomes['Ana'])
else:
    print("Não encontrado")

#Vai escrever no console os números divisíveis por 5.
inicio = 0
fim = 10

for numero in range(inicio, fim):
    if numero % 5 == 0:
        print(numero)