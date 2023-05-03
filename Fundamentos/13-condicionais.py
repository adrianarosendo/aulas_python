idade = int(input("Insira sua idade: "))

if idade >= 18:
    print("Você é maior de idade!")
else:
    print("Você é menor de idade!")


nota1 = float(input("Insira sua nota 1: "))
nota2 = float(input("Insira sua nota 2: "))
nota3 = float(input("Insira sua nota 3: "))

media = (nota1 + nota2 + nota3)/3

if media == 10:
    print("Parabéns você passou com nota máxima! Sua média foi: ", media)
elif media >= 7:
    print("Parabéns, você passou! Sua média foi: ", media)
else:
    print("Você está de recuperação! Sua média foi: ", media)