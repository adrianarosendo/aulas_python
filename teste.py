import random

def gerar_historia():
    sujeitos = ["João", "Maria", "O gato", "O cachorro", "Um alienígena"]
    verbos = ["correu", "saltou", "voou", "brincou", "conversou"]
    objetos = ["no parque", "na floresta", "na lua", "no supermercado", "no castelo"]
    conclusoes = ["e todos viveram felizes para sempre.", "e nunca mais foram vistos novamente.", "e aprenderam uma grande lição."]

    sujeito = random.choice(sujeitos)
    verbo = random.choice(verbos)
    objeto = random.choice(objetos)
    conclusao = random.choice(conclusoes)

    historia = f"{sujeito} {verbo} {objeto}, {conclusao}"
    return historia


print("Bem-vindo ao Gerador de Histórias Aleatórias!")
print("Aqui está a sua história:")
print(gerar_historia())






