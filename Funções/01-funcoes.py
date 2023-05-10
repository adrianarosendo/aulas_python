#Recebendo informação do usuário
numero = input("Insira um número: ")

#Definição da função
def soma_algarismos():
    soma_total = 0
    for i in range(0, len(numero)):
        soma_total = int(numero[i]) + soma_total
    return print("Soma dos algarismo é igual a:", soma_total)

#Chamada da função
soma_algarismos()


