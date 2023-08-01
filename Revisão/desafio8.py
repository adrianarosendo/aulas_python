#Crie um programa que o usuário deverá adivinhar o número que o computador está "pensando"
#Use o while 


while True:
    numero = int(input("Tente adivinhar o número que eu estou pensando: "))
    if numero == 32:
        print("Parabéns você acertou!")
        break

    