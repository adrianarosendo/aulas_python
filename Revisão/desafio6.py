#a partir das listas abaixo faça um sistema que efetue todas as combinações das listas com cor 
#primeiro lugar

cores = ["amarelo", "azul", "vermelho", "verde", "preto"]
tipos = ["claro", "escuro", "pastel", "metálico"]

for cor in cores:
    for tipo in tipos:
        print(cor, tipo)
    