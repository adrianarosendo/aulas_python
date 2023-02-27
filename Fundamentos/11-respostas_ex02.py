estudo_terca = False
estudo_quinta = False

nota10 = estudo_quinta and estudo_terca
nota8 = estudo_terca != estudo_quinta
passeio = estudo_terca or estudo_quinta
ficar_em_casa = not passeio
reprovado = not passeio

print("Nota 10={} Nota 8={} Passeio={} Ficar em casa={} Reprovado={}"
      .format(nota10, nota8, passeio, ficar_em_casa, reprovado))