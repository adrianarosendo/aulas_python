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

numeros = '1234567890'

print(numeros[::])
print(numeros[::2])
print(numeros[1::2])
print(numeros[::-1])
print(numeros[::-2])

print(nome[::-1])

frase = 'Python é uma linguagem excelente'
#'py' not in frase
#'ing' in frase
len(frase)
frase.lower()
print(frase)
frase = frase.upper()
print(frase)

frase.split()
frase.split('E')

# dir(str)
# help(str.center)

# %%
a = '123'
b = ' de Oliveira 4'
print(a + b)
a.__add__(b)
str.__add__(a, b)

len(a)
a.__len__()
#'1' in a
a.__contains__('1')

dir(str)