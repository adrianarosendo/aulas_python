#Crie um dicionário com 5 países e 5 capitais, peça para o usuário digitar um país e mostre sua capital
#Se caso o país não estiver na lista, escreva essa informação para o usuário

paises = {"Argentina" : "Buenos Aires",
          "Brasil" : "Brasília",
          "Itália" : "Roma",
          "Espanha" : "Madri",
          "Alemanha" : "Berlim"

}

pais_usuario = input("Digite um país: ")

if pais_usuario in paises:
    print(f"A capital do país digitado é: {paises[pais_usuario]}")
else:
    print("Não temos informação sobre esse país!")