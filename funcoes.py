# Funções estão diretamente relacionados a rotinas de código que podem ser reutilizadas diversas vezes ao longo do programa.

def lin(frase: str):
    print('-' * 45)
    print(frase.center(45))
    print('-' * 45)


lin(frase = 'SISTEMAS DE ALUNOS')
lin('CADASTRO DE FUNCIONÁRIOS')
lin('ERRO DE SISTEMA')




# O * representa que a função pode receber uma quantidade variável de argumentos, ou seja, não é necessário definir quantos argumentos serão passados para a função.
def contador(* num: int):
    for i in num:
        # Esse último parâmetro 'end' serve para que o print não pule linha após a exibição do valor
        print(i, end='')

contador(1, 2, 3)
contador(4, 5, 6, 7, 8)
contador(9, 10)



# Criando uma função que dobra valores em uma lista
def dobravalores(lista: list):
    valor_dobrado: list = []
    for i in range(0, len(lista)):
        resultado = lista[i] * 2
        valor_dobrado.append(resultado)
        print(f'O valor passado foi {lista[i]} o valor final é {valor_dobrado[i]}')
    return valor_dobrado

dobrar: list = [1, 2, 3, 4, 5]
dobravalores(dobrar)