import random

# Lista de palavras
palavras = ["python", "programacao", "desafio", "forca"]

# Escolher uma palavra aleatória
palavra_secreta = random.choice(palavras)
letras_adivinhadas = ["_"] * len(palavra_secreta)
tentativas = 6

# Jogo
while tentativas > 0 and "_" in letras_adivinhadas:
    print("Palavra: ", " ".join(letras_adivinhadas))
    letra = input("Digite uma letra: ").lower()

    if letra in palavra_secreta:
        for i in range(len(palavra_secreta)):
            if palavra_secreta[i] == letra:
                letras_adivinhadas[i] = letra
    else:
        tentativas -= 1
        print(f"Você errou! Tentativas restantes: {tentativas}")

    if "_" not in letras_adivinhadas:
        print("Parabéns! Você adivinhou a palavra:", palavra_secreta)
        break

if tentativas == 0:
    print(f"Você perdeu! A palavra era: {palavra_secreta}")
