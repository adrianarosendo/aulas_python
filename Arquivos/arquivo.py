# pylint: disable=unspecified-encoding
#cria um arquivo caso não exista
#ou substitui o atual
arquivo = open('arquivo.txt', 'w')

#mostra um erro quando um arquivo não exista
#modo somente leitura
arquivo = open('arquivo.txt', 'r')

#mostra um erro quando um arquivo não exista
#modo somente escrita
arquivo = open('arquivo.txt', 'x')
arquivo.close()

