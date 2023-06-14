contar = ['zero','um', 'dois', 'três', 'quatro', 'cinco',
'seis', 'sete', 'oito', 'nove', 'dez', 'onze','doze',
'treze','quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito',
'dezenove', 'vinte', 'vinte e um', 'vinte e dois', 'vinte e três', 'vinte e quatro',
'vinte e cinco', 'vinte e seis', 'vinte e sete', 'vinte e oito', 'vinte e nove', 'trinta']


while True:
    numero = int(input("Digite um número de 0 até 30:"))
    if 0 <=  numero <= 30:
        break
    print('Tente novamente...')    
print("Seu número foi: ", contar[numero])