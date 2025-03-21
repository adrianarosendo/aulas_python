#Trabalhando com Strings

nome = 'Saulo Pedro'

print(nome[0])

texto = 'Texto entre apostrófos pode ter "aspas"'

doc = """Texto com múltiplas
    ... linhas"""

print('Texto com múltiplas\n\t... linhas')
print(doc)

doc2 = '''Também é possível
... com 3 aspas simples'''


nome = 'Ana Paula'
print(nome[0])
print(nome[6])
print(nome[-3])
print(nome[4:])
print(nome[-5:])
print(nome[:3])
print(nome[2:5])
print(nome[::-1])

frase = 'Python é uma linguagem excelente'
print(len(frase))
frase = frase.lower()
print(frase)
frase = frase.upper()
print(frase)

frase = frase.split()
print(frase)
frase = 'Python é uma linguagem excelente'
frase = frase.split('e')
print(frase)

a = '123'
b = ' de Oliveira 4'
print(a + b)


print(len(a))


print(a.__contains__('1'))

lista_de_frutas = ["banana", "laranja", "uva", "maça"]
lista_de_frutas.sort()
print(lista_de_frutas)
lista_de_frutas.reverse()
print(lista_de_frutas)
lista_de_frutas.append("limão")
print(lista_de_frutas)
print(lista_de_frutas.__contains__('banana'))
print(lista_de_frutas.__contains__('manga'))
lista_de_frutas.remove('maça')
print(lista_de_frutas)
lista_de_frutas.pop()
print(lista_de_frutas)
print(lista_de_frutas.count('banana'))
print(len(lista_de_frutas))