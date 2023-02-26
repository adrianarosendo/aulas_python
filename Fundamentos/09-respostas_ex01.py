#Desafio 1
#Agora que conhecemos os operadores aritméticos do Python, 
#faça o calculo utilizando o que aprendemos em aula e diga
#quantos % representa a despesa mencionada abaixo, comparada com a receita.

salario = 12327.60
despesas = 8767.40

#Resposta
percentual = (despesas / salario) * 100
print('Seu percentual usado do salário é de %.2f'%(percentual),"%")

#Desafio 2
#Faça o calculo de uma idade a partir de um ano inserido pelo usuário.

ano_nascimento = input('Diga em que ano você nasceu que te direi sua idade?')
atual = 2023
idade = atual - int(ano_nascimento)


#Resposta

print('Você tem' , idade , 'anos!')