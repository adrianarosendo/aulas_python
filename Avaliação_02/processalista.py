# Encontra e retorna o maior número impar presente na lista
def maior_impar(lista):
    lista.sort()
    while lista:
        numero = max(lista)
        if numero % 2 == 0:
            lista.remove(numero)
        else:
            return numero

# Encontra e retorna o menor número impar presente na lista
def menor_impar(lista):
    lista.sort()
    while lista:
        numero = min(lista)
        if numero % 2 == 0:
            lista.remove(numero)
        else:
            return numero

# Encontra e retorna o maior e o menor número ímpar presentes na lista
def menor_maior_impar(lista):
    return menor_impar(lista),maior_impar(lista)

lista_teste = [9,5,3,4,2,7,0,17,2,3,23,955,1]
print(maior_impar(lista_teste))
print(menor_impar(lista_teste))
print(menor_maior_impar(lista_teste))