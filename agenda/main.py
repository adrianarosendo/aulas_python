from agenda import Pessoa

lista_agenda = []

while True:
    instrucao = int(input("Digite o número da opção:\n 1 - adicionar\n 2- excluir agenda\n 3- Remover contato\n 4 - imprimir contatos\n"))
    if instrucao == 1:
        pessoa1 = Pessoa(nome = input("Digite o nome"),idade = input("Digite a idade"), telefone = input("Digite o telefone"), endereço = input("Digite o endereço"))
        lista_agenda.append(pessoa1)
    elif instrucao == 2:
       lista_agenda = []
    elif instrucao == 3:
        remover=int(input("Digite o número do contato que você quer remover: "))
        lista_agenda.pop(remover)
    elif instrucao == 4:
        for item in lista_agenda:

            print(item.nome)
            print(item.idade)
            print(item.telefone)
            print(item.endereço)