import random

def sortear_nome(lista_nomes):
    return random.choice(lista_nomes)

# Entrada do usuário
nomes = input("Digite os nomes separados por vírgula: ").split(",")

# Removendo espaços extras
nomes = [nome.strip() for nome in nomes]

# Sorteio e exibição do resultado
sorteado = sortear_nome(nomes)
print(f"O nome sorteado foi: {sorteado}")