# Exemplo de criação de sets.
numeros = [1, 2, 2, 3, 3, 3]
numeros_distintos = set(numeros)
print("Números: ", numeros)
print("Números distintos: ", numeros_distintos)

# Exemplo de criação de sets.
numeros = [1, 2, 2, 3, 3, 3]
numeros_distintos = set() 
for num in numeros:
    numeros_distintos.add(num) 
print("Números: ", numeros)
print("Números distintos: ", numeros_distintos)

#usando a função remove
nums = set([1, 2, 2, 3, 3, 3])
nums.remove(2)
print("Números: ", nums)

#usando a função discard (não retorna erro)
nums = set([1, 2, 2, 3, 3, 3])
nums.discard(4) 
nums.discard(2)
print(nums)

#limpando toda a lista
nums = set([1, 2, 2, 3, 3, 3])
print("Números: ", nums)
nums.clear()
print("Números: ", nums)

#união de conjuntos
A = {0, 1, 3, 5, 7, 9} 
B = {0, 2, 4, 6, 8}
C = A.union(B)
print(C)

#interseção de conjuntos
A = {0, 1, 3, 5, 7, 9}
B = {0, 2, 4, 6, 8}
C = A.intersection(B) 
print(C)