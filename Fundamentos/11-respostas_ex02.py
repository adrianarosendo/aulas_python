

#Estudos
estudo_terca = int(input("Você estudou terça?"))
estudo_quinta = int(input("Você estudou quinta?"))
estudo_terca = bool(estudo_terca)
estudo_quinta = bool(estudo_quinta)

print(estudo_quinta)
print(estudo_terca)

#Resultados
nota10 = estudo_quinta and estudo_terca
nota8 = estudo_terca != estudo_quinta
passeio = estudo_terca or estudo_quinta
ficar_em_casa = not passeio
reprovado = not passeio

#Impressão
print("Nota 10={} Nota 8={} Passeio={} Ficar em casa={} Reprovado={}"
      .format(nota10, nota8, passeio, ficar_em_casa, reprovado))

#interpolação .format



valor1= int(input("Insira o primeiro número."))
valor2 = int(input("Insira o segundo número."))

print("Soma é igual a", valor1 + valor2)
print("Subtração é igual a", valor1 - valor2)
print("Multiplicação é igual a", valor1 * valor2)
print("Divisão é igual a", valor1 / valor2)