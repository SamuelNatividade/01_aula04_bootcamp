import csv

caminho_do_arquivo: str = "exemplo.csv"

arquivo_csv: list = []

# gerenciador de contextos
# lendo um arquivo csv somente com as bibliotecas nativas do python
with open(file = caminho_do_arquivo, mode = "r", encoding = "utf-8") as arquivo:
    leitor_csv = csv.DictReader(arquivo)
    for linha in leitor_csv:
        arquivo_csv.append(linha)
print(arquivo_csv)

 