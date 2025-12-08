import csv

caminho_arquivo: str = r"C:\Users\eduar\Downloads\Crawler Failed.csv"

# Inicializa uma lista vazia para armazenar os dados do CSV
dados: list = []

# Usa o gerenciador de contexto 'with' para abrir o arquivo
with open(caminho_arquivo, mode='r', encoding='utf-8') as arquivo_csv:
    # cria um objeto leitor de CSV. Por isso precisa ser convertido em uma lista de dicionários
    leitor_csv = csv.DictReader(arquivo_csv)

    # Itera sobre as linhas do arquivo CSV
    for linha in leitor_csv:
        # Adiciona cada linha (um dicionário) à lista de dados
        dados.append(linha)

# Exibe os dados lidos do arquivo CSV
for i, registro in enumerate(dados):
    print(i, dados[i]['Link Competitor'])