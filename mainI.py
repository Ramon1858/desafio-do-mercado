import meu_modulo1

def mercado():
    nome = input('digite seu nome:')
    meu_modulo1.display1(nome)
    lista_produtos = ['0- chocolate', '1-bala','2-chiclete']
    lista_valores = [15.0,1.0,2.0]
    c = meu_modulo1.carrinho(lista_produtos,lista_valores)
    print(c)
mercado()
print('muito obrigado,volte sempre')