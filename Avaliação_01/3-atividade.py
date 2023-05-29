# declaração das variáveis
inicio = 0
fim = 1000
divisor = int(input("Digite o divisor que queira verificar:"))

for numero in range(inicio, fim):
    if numero % divisor == 0:
        print(numero)
 