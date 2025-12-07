import json


carrinho: list = []

produto_1: dict = {
    'Nome': 'Televisão',
    'Quantidade': 2,
    'Preco': 3000.00,
    'Disponibilidade': True
}

produto_2: dict = {
    'Nome': 'Sapato',
    'Quantidade': 10,
    'Preco': 75.00,
    'Disponibilidade': True
}

carrinho.append(produto_1)
carrinho.append(produto_2)


carrinho_json = json.dumps(carrinho)
print(carrinho_json)