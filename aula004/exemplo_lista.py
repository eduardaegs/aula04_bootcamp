produto: str = 'Sapato'
produto_2: str = 'Camiseta'
produto_3: str = 'Calça'

produtos: list = []

produtos.append(produto)
produtos.append(produto_2)
produtos.append(produto_3)
produtos.pop() # Melhor em performance pois um lista.remove(item) gastaria mais processamento do que somente excluir o último valor
produtos.pop()

print(produtos)