class Pessoa:
    def __init__(self, nome, idade, comendo=False, falando=False, andando=False):
       self.nome = nome
       self.idade = idade
       self.comendo = comendo
       self.andando = andando
       self.falando = falando

    def comer(self, comida):
        if self.comendo == True:
            return print(f"{self.nome} já está comendo!")
        if self.falando == True:
            return print(f"{self.nome} está falando, termine antes de comer!")
        print(f"{self.nome} está comendo", comida)
        self.comendo = True

    def parar_de_comer(self):
        if not self.comendo:
            return print(f"{self.nome} não está comendo!")
        self.comendo = False
        print(f"{self.nome} parou de comer!")

    def falar(self, frase):
        if self.comendo == True:
            return print("Não se pode falar de boca cheia!")
        print(f"{self.nome}: {frase}")
        self.falando = True

    def parar_de_falar(self):
        if not self.falando:
            return print(f"{self.nome} não está falando!")
        self.falando = False
        print(f"{self.nome} parou de falar!")

