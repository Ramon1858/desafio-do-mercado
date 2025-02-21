def display(nome):
    print('olá,seja bem vindo(a)',nome)

def carrinho(produtos,precos):
    meu_carrinho = []
    valores = []
    p = input('deseja fazer seu pedido s/n:')
    while p == 's':
        
        pedido = int(input('digite seu produto pelo id:'))
        print('0- chocolate', '1-bala','2-chiclete')
        meu_carrinho.append(pedido)
        valores.append(precos[pedido])
        total = sum(valores)
        print('***' * 35)
        print(total)
        p = input('deseja fazer o pedido?s/n:')
    return meu_carrinho