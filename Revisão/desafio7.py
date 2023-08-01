#Você é dono de uma loja, crie uma lista com 10 produtos que você possui em estoque,
#Peça para o usuário digitar um produto e verifique se você possui em estoque
#Caso positivo responda via console "Produto em estoque", caso negativo responda via console
#"No momento não temos esse produto!"

doces = ["bolo", "cupcake", "biscoito", "brigadeiro", "beijinho"]

pedido = input("Bem vindo a loja de doces, faça seu pedido:")


if pedido in doces:
    print("Produto em estoque")
else:
    print("No momento não temos esse produto!")
