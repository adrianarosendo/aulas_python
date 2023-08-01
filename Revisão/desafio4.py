#A partir do desafio anterior, altere o segundo elemento da lista ordenada de frutas para "tomate"
#Imprima a lista no console
#Agora, remova o último item da lista e imprima no console


fruta1 = input("Digite a primeira fruta: ")
fruta2 = input("Digite a segunda fruta: ")
fruta3 = input("Digite a terceira fruta: ")
fruta4 = input("Digite a quarta fruta: ")
fruta5 = input("Digite a quinta fruta: ")

lista_frutas = [fruta1, fruta2, fruta3, fruta4, fruta5]

lista_frutas.sort()

print(lista_frutas)

lista_frutas[1] = "tomate"

print(f"Alteração: {lista_frutas[1]}")
print(f"Lista: {lista_frutas}")

lista_frutas.remove(lista_frutas[-1])

print(f"Lista: {lista_frutas}")