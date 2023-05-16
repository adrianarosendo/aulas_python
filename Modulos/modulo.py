# pylint: disable=import-error
import area

print("Vamos calcular a área de formas geométricas!\n")

def calcula_area(n_forma):
    if n_forma == "quadrado":
        lado = float(input("Insira o valor do lado do quadrado que deseja calcular: "))
        print("A área calculada é de:", area.area_quadrado(lado))
    elif n_forma == "circulo":
        raio = float(input("Insira o valor do raio do circulo que deseja calcular: "))
        print("A área calculada é de:", area.area_circulo(raio))
    elif n_forma == "triangulo":
        base = float(input("Insira o valor da base do triângulo que deseja calcular: "))
        altura = float(input("Insira o valor da altura do triângulo  que deseja calcular: "))
        print("A área calculada é de:", area.area_triangulo(base, altura))
    else:
        print("Forma não localizada!")
        inicio()

def inicio():
    forma = input("Digite o nome da forma que deseja calcular a área: ")
    calcula_area(forma)


inicio()