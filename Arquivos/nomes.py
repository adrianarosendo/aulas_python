#Vamos criar uma variável para ler um arquivo
arquivo = open('nomes.txt', 'r')
linhas = arquivo.read()
arquivo.close()
#essa variável vai ser do tipo str
print(linhas)

#novamente lendo o arquivo e usando o readlines
arquivo = open('nomes.txt', 'r')
linhas = arquivo.readlines()
arquivo.close()
#essa variável vai ser do tipo list
print(linhas)

#imprimindo em lista
arquivo = open('nomes.txt', 'r')
linhas = arquivo.readlines()
arquivo.close()
for linha in linhas:
    print(linha)
#essa variável vai ser do tipo list
print(linhas)

#Fazendo calculos com valores do arquivo
soma = 0
arquivo = open('nomes.txt', 'r')
linhas = arquivo.readlines()
arquivo.close()
for linha in linhas:
    pessoas = linha.split(' ')
    idade = int(pessoas[-1])
    print(int(idade))
    soma = soma+idade
    media = (soma) / len(linhas)
    
print(media)

#como escrever em um arquivo
arquivo = open('nomes.txt', 'a')
arquivo.write('Thiago; estudante; 15')
arquivo.close()
