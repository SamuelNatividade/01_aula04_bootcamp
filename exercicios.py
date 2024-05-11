## 1. Crie uma lista com os números de 1 a 10 e use um loop para imprimir cada número elevado ao quadrado.
numeros = range(1,11)
for i in numeros:
    print(i**2)

## 2. Dada a lista ["Python", "Java", "C++", "JavaScript"], remova o item "C++" e adicione "Ruby".
lista_1 = ["Python", "Java", "C++", "JavaScript"]
lista_1.remove("C++")
lista_1.append("Ruby")
print(lista_1)

## 3. Crie um dicionário para armazenar informações de um livro, incluindo título, autor e ano de publicação. Imprima cada informação.
livro: dict = {
    'Titulo':'Game of thrones',
    'Autor':'george martin',
    'Ano': 2010
}
## para printar os elementos de um dicionario 
elementos_dic: list = livro.items()
for elemento in elementos_dic:
    print(elemento)

## 4. Escreva um programa que conta o número de ocorrências de cada caractere em uma string usando um dicionário.
def contar_ocorrencias(string):
    ocorrencias = {}

    for caractere in string:
        if caractere in ocorrencias:
            ocorrencias[caractere] += 1
        else:
            ocorrencias[caractere] = 1

    return ocorrencias

# # Exemplo de uso
string = "banana"
resultado = contar_ocorrencias(string)
print("Ocorrências de cada caractere em '{}':".format(string))
for caractere, ocorrencias in resultado.items():
    print("'{}' ocorre {} vezes.".format(caractere, ocorrencias))


## 5. Dada a lista ["maçã", "banana", "cereja"] e o dicionário {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}, calcule o preço total da lista de compras.
dict_ = {"maca": 0.45, "banana": 0.30, "cereja": 0.65}
lista_2 = ["maca", "banana", "cereja"]
preco_total = 0 
for produto, preco in dict_.items():
    preco_total += preco
print(f"o preco total da cesta de compras é {preco_total}")
    


## 6. Eliminação de Duplicatas (eliminar duplicadas de uma lista)
emails = ["user@example.com", "admin@example.com", "user@example.com", "manager@example.com"]
emails_distinct = list(dict.fromkeys(emails))
print(emails_distinct)

## 7. Objetivo: Dada uma lista de idades, filtrar apenas aquelas que são maiores ou iguais a 18.
import random
idades = []
for _ in range(50):
    idade = random.randint(1,100)
    idades.append(idade)

maior_idade = [idade for idade in idades if idade >= 18]

## 8. Objetivo: Dado um conjunto de números, calcular a média.
soma = sum(idades)
contagem = len(idades)
media = round(soma/contagem, 2)
print(f"a media de idade é de {media}")



## 9. Dada uma lista, dividir em duas listas, uma para valores pares e outros impares
pares = [i for i in idades if i % 2 == 0]
impares = [i for i in idades if i % 2 != 0]

print("Pares: ", pares)
print("Impares: ", impares)
