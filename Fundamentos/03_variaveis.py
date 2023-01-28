# O Python usa o = para atribuir valores a variáveis.
# Não há como declarar uma variável sem atribuir um valor inicial a ela.

numero1 = 10

numero2 = 5

print(numero1 + numero2)

#interpretador fortemente tipada, ele entende o tipo
numero1 = 'Sou um texto!'

print(numero1)

# Inteiro
a = 2
print(a)
print(type(a))


# Inteiro
b = 9223372036854775807
print(b)
print(type(b))


# Ponto flutuante ou decimal
pi = 3.14
print(pi)
print(type(pi))


# String ou texto
c = 'A'
print(c)
print(type(c))


# String
name = 'Colégio São Mauro'
print(name)
print(type(name))

# Boolean
q = True
print(q)
print(type(q))


# Valor vazio ou tipo de dados nulo
x = None
print(x)
print(type(x))

x = True # válido
y = True # válido

#Atribuindo valores a várias variáveis em uma linha
x, y, z = 1,2,3

#Essa variável dummy pode ter qualquer nome, mas é convencional 
#usar o underline _ para atribuir valores:
x,y,_ = 1,2,3

#Atenção, eu não posso fazer isso aqui.

#  9x = False # começando com um número
# => SyntaxError: invalid syntax

#  $y = False # começando com um símbolo
# => SyntaxError: invalid syntax