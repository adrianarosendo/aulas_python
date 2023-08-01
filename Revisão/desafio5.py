#A partir do desafio anterior, faça um for e imprima todos os itens da lista, um por um, na frase
# "Eu vou na feira comprar: {nome da fruta}"

fruta1 = input("Digite a primeira fruta: ")
fruta2 = input("Digite a segunda fruta: ")
fruta3 = input("Digite a terceira fruta: ")
fruta4 = input("Digite a quarta fruta: ")
fruta5 = input("Digite a quinta fruta: ")

lista_frutas = [fruta1, fruta2, fruta3, fruta4, fruta5]
for fruta in lista_frutas:
    print(f"Eu vou na feira comprar: {fruta}")
