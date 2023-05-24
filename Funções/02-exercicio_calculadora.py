# Definição das funções
def soma(valor1, valor2): return valor1 + valor2
def divisao(valor1, valor2): return valor1 / valor2
def multiplicacao(valor1, valor2): return valor1 * valor2
def subtracao(valor1, valor2): return valor1 - valor2

def chamada_calculadora(operacao, numero1, numero2):
    if operacao == "+":
        print(soma(numero1, numero2)) 
    elif operacao == "*":
        print(multiplicacao(numero1, numero2)) 
    elif operacao == "/":
        print(divisao(numero1, numero2)) 
    elif operacao == "-":
        print(subtracao(numero1, numero2)) 
    else:
        print("Nenhuma operação válida detectada, tente novamente.")
        inicio_calculadora()

def inicio_calculadora():
    numero1 = int(input("Digite o primeiro número: "))
    operacao = input("Digite o número da operação desejada: + para soma, - para subtração, * para multiplicação ou / para divisão: ")
    numero2 = int(input("Digite o segundo número: "))  
    chamada_calculadora(operacao, numero1, numero2)
   
# Chamada da calculadora
inicio_calculadora()


