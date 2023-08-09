from pessoa import Pessoa

pessoa1 = Pessoa("Luiz", 35)
pessoa2 = Pessoa("Ana", 42)

print(pessoa1.nome)
pessoa1.parar_de_comer()
#é um atributo para pessoa 1
#pessoa1.nome = "Luiz"
#p2.nome = "Joaquim"
print(pessoa1.comendo)
pessoa1.comer("banana")
print(pessoa1.comendo)
pessoa1.comer("laranja")
pessoa1.falar("Olá classe!")
pessoa1.parar_de_comer()
pessoa1.falar("Olá classe!")

#print(pessoa1.nome, p2.nome)

#pessoa1.falar()

#pessoa1 é um instancia dessa classe Pessoa


