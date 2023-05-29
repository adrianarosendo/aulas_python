# variáveis do tipo string
nome = 'João da Silva'
cidade = 'São Paulo'
cpf = '123.456.789-00'
caractere = ".-"

#variáveis em maiúsculo
print(nome.upper(), cidade.upper(), cpf.upper())

#variáveis em minúsculo

print(nome.lower(), cidade.lower(), cpf.lower())

#Exiba a posição do caractere ã, se presente, em cada uma das variáveis;

print("Posição ã na variável nome", nome.find("ã"))
print("Posição ã na variável cidade",cidade.find("ã"))
print("Posição ã na variável cpf",cpf.find("ã"))

# Exiba o número de caracteres de cada variável;
print(len(nome))
print(len(cidade))
print(len(cpf))


#Remova os pontos (.) e o hífen (–) da variável cpf.

for i in range(0,len(caractere)):
    cpf = cpf.replace(caractere[i],"")
    
print(cpf)
