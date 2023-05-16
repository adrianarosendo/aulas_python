import math
from datetime import datetime, timedelta
import itertools
import random

#número de pi
print(math.pi)

#raiz quadrada
print(math.isqrt(4))

#potência
print(math.pow(2, 2))

#Buscando o dia de hoje
print(datetime.today())
#Somando 7 dias
print(datetime.today() + timedelta(days=7))

#combinação de 2 em 2
aleatorio = list(itertools.combinations("ABCD", 2))
print(aleatorio)

#permutação de 2 em 2
aleatorio = list(itertools.permutations("ABCD", 2))
print(aleatorio)

print("Numúmero aleatório entre 0 e 10:", random.randint(0,10))

valor = ["sim", "não"]
k = 1
 
print(random.SystemRandom().sample(valor, k))