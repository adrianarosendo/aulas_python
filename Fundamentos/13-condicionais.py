#Verifica se a pessoa é maior ou menor de idade
idade = int(input("Insira sua idade: "))

if idade >= 18:
    print("Você é maior de idade!")
else:
    print("Você é menor de idade!")

#Calcula a média do aluno a partir de 3 notas digitadas pelo usuário
nota1 = float(input("Insira sua nota 1: "))
nota2 = float(input("Insira sua nota 2: "))
nota3 = float(input("Insira sua nota 3: "))

def calcula_media(n1, n2, n3):
    return (n1 + n2 + n3)/3

media = calcula_media(nota1, nota2, nota3)

if media == 10:
    print("Parabéns você passou com nota máxima! Sua média foi: ", media)
elif media >= 7:
    print("Parabéns, você passou! Sua média foi: ", media)
else:
    print("Você está de recuperação! Sua média foi: ", media)