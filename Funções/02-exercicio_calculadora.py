# Definição das funções
def soma(valor1, valor2): return valor1 + valor2
def divisao(valor1, valor2): return valor1 / valor2
def multiplicacao(valor1, valor2): return valor1 * valor2

def chamada_calculadora(operacao, numero1, numero2):
    if operacao == 1:
        print(soma(numero1, numero2)) 
    elif operacao == 2:
        print(multiplicacao(numero1, numero2)) 
    elif operacao == 3:
        print(divisao(numero1, numero2)) 
    else:
        print("Nenhuma operação válida detectada, tente novamente.")
        inicio_calculadora()

def inicio_calculadora():
    operacao = int(input("Digite o número da operação desejada: 1 para soma, 2 para multiplicação ou 3 para divisão: "))
    numero1 = int(input("Digite o primeiro número: "))
    numero2 = int(input("Digite o segundo número: "))  
    chamada_calculadora(operacao, numero1, numero2)
   
# Chamada da calculadora
inicio_calculadora()


