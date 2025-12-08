def dobravalores(lista: list):
    valor_dobrado: list = []
    for i in range(0, len(lista)):
        resultado = lista[i] * 2
        valor_dobrado.append(resultado)
        print(f'O valor passado foi {lista[i]} o valor final é {valor_dobrado[i]}')
    print(f'Lista final: {valor_dobrado}')

dobrar: list = [1, 2, 3, 4, 5]
dobravalores(dobrar)