#Desafio 1
#Agora que conhecemos os operadores aritméticos do Python, 
#faça o calculo utilizando o que aprendemos em aula e diga
#quantos % representa a despesa mencionada abaixo, comparada com a receita.

salario = 12327.60
despesas = 8767.40



#Desafio 2
#Faça o calculo de uma idade a partir de um ano inserido pelo usuário.

ano_nascimento = input('Diga em que ano você nasceu que te direi sua idade?')


titulos = ["a", "b", "o", "ab", "c"]
palavra = "o"

contador = 0
for titulo in titulos:
    # Convertendo o título para letras minúsculas para fazer a contagem sem diferenciação de maiúsculas/minúsculas
    if palavra.lower() in titulo.lower():
        contador += 1


print(f'A palavra "{palavra}" aparece nos títulos {contador} vezes.')

titulos_ordenados = sorted(titulos)
titulos.sort()
titulos.reverse()
print(titulos_ordenados)
print(titulos)