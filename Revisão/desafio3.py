#Crie uma lista com 5 frutas que o usuário enviar via input e organize em ordem crescente.
#Imprima em tela as informações

fruta1 = input("Digite a primeira fruta: ")
fruta2 = input("Digite a segunda fruta: ")
fruta3 = input("Digite a terceira fruta: ")
fruta4 = input("Digite a quarta fruta: ")
fruta5 = input("Digite a quinta fruta: ")

lista_frutas = [fruta1, fruta2, fruta3, fruta4, fruta5]

lista_frutas.sort()

print(lista_frutas)

