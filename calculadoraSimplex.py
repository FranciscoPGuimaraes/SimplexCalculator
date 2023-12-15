"""
@authors Francisco P. Guimarães, Laura Pivoto Ambrósio, Rodrigo Paiva Oliveira (Zenks)
"""
import numpy as np
from tabulate import tabulate

print("""----------- SIMPLEX CALCULATOR  ----------
OBS: Entrar com o PPL na forma padrão e ignorar a restrição de não negatividade""")

# Entrada do usuário para o número de variáveis e restrições
qtd_variaveis = int(input("Número de variáveis: "))
qtd_restricoes = int(input("Número de restrições: "))

# Inicialização da matriz de coeficientes do modelo de PPL
matriz_coeficientes = np.zeros((qtd_restricoes + 1, qtd_variaveis + qtd_restricoes + 1))
matriz_labels = np.zeros((qtd_restricoes + 1, 1))

# Entrada dos coeficientes da matriz de lucro
coeficientes_lucro = list(map(float, input("Digite os coeficientes de lucro separados por espaço: ").split()))
matriz_coeficientes[0, :qtd_variaveis] = coeficientes_lucro

# Entrada dos coeficientes das variáveis e restrições
for i in range(qtd_restricoes):
    coeficientes_variaveis = list(map(float, input(
        f"Digite os coeficientes das variáveis para a restrição {i + 1} separados por espaço: ").split()))
    sinal = int(input("Sinal da restrição (<) digite 0 e (>) digite (1): "))
    matriz_coeficientes[i + 1, :qtd_variaveis] = coeficientes_variaveis
    if sinal == 1:
        matriz_coeficientes[i + 1, qtd_variaveis + i] = -1  # Variável auxiliar
    else:
        matriz_coeficientes[i + 1, qtd_variaveis + i] = 1  # Variável auxiliar

# Entrada dos coeficientes das constantes das restrições
coeficientes_restricoes = "0 " + input("Digite os coeficientes das constantes das restrições separados por espaço: ")
coeficientes_restricoes = list(map(float, coeficientes_restricoes.split()))
matriz_coeficientes[:, -1] = coeficientes_restricoes

# Calculando número mais negativo e sua coluna na primeira linha
numero_mais_negativo = matriz_coeficientes[0, 0]
coluna_numero_mais_negativo = 0

for coluna, elemento in enumerate(matriz_coeficientes[0, :]):
    if elemento < numero_mais_negativo:
        numero_mais_negativo = elemento
        coluna_numero_mais_negativo = coluna

contador = 0

while numero_mais_negativo < 0:
    # Calculando o pivo
    ultima_coluna = qtd_variaveis + qtd_restricoes
    if matriz_coeficientes[1, coluna_numero_mais_negativo] != 0:
        menor_numero = matriz_coeficientes[1, ultima_coluna] / matriz_coeficientes[1, coluna_numero_mais_negativo]
    else:
        menor_numero = np.inf
    linha_pivo = 1

    # Percorrendo a última coluna a partir da segunda linha
    for linha in range(2, qtd_restricoes + 1):
        # Calculando a divisão para encontrar o menor número
        if matriz_coeficientes[linha, coluna_numero_mais_negativo] != 0:
            divisao = matriz_coeficientes[linha, ultima_coluna] / matriz_coeficientes[linha, coluna_numero_mais_negativo]
        else:
            divisao = np.inf

        # Atualizando se encontrarmos um número menor
        if divisao < menor_numero and divisao > 0:
            menor_numero = divisao
            linha_pivo = linha

    valor_pivo = matriz_coeficientes[linha_pivo, coluna_numero_mais_negativo]
    matriz_labels[linha_pivo, 0] = coluna_numero_mais_negativo + 1

    # Dividindo a linha pivo pelo pivo
    matriz_coeficientes[linha_pivo, :] /= valor_pivo

    # Calculando as novas linhas
    for linha in range(0, qtd_restricoes + 1):
        if linha != linha_pivo:
            # Coeficiente correspondente na coluna do pivô
            coeficinte_correspondente = matriz_coeficientes[linha, coluna_numero_mais_negativo]

            # Atualizando a linha
            colunas = qtd_variaveis + qtd_restricoes + 1
            for valor in range(colunas):
                matriz_coeficientes[linha, valor] -= coeficinte_correspondente * matriz_coeficientes[linha_pivo, valor]

    # Mostrando a matriz
    contador += 1
    print(f"Matriz {contador}:")
    print(tabulate(matriz_coeficientes, headers="firstrow", tablefmt="fancy_grid"))

    # Calculando número mais negativo e sua coluna na primeira linha
    numero_mais_negativo = matriz_coeficientes[0, 0]
    coluna_numero_mais_negativo = 0

    for coluna, elemento in enumerate(matriz_coeficientes[0, :]):
        if elemento < numero_mais_negativo:
            numero_mais_negativo = elemento
            coluna_numero_mais_negativo = coluna

print("----------- RESULTADOS -----------\n")

# Mostrando a matriz final
print("Matriz após a divisão da linha pivô pelo valor do pivô:")
print(tabulate(matriz_coeficientes, headers="firstrow", tablefmt="fancy_grid"))

# Lucro ótimo
ultima_coluna = qtd_variaveis + qtd_restricoes
print(f"\nLucro ótimo: R$ {matriz_coeficientes[0, ultima_coluna]:.2f}")

# Pontos ótimos
print("\nPontos ótimos:")
header = ["Variável", "Valor"]
data = []
for i in range(qtd_restricoes + 1):
    if matriz_labels[i, 0] != 0 and matriz_labels[i, 0] <= qtd_variaveis:
        data.append([f"Variável {int(matriz_labels[i, 0])}", f"{matriz_coeficientes[i, ultima_coluna]:.2f}"])
print(tabulate(data, headers=header, tablefmt="fancy_grid"))

# Preço sombra
print("\nPreço sombra das restrições:")
header = ["Restrição", "Valor"]
data = [[f"Restrição {i + 1}", matriz_coeficientes[0, qtd_variaveis + i]] for i in range(qtd_restricoes)]
print(tabulate(data, headers=header, tablefmt="fancy_grid"))
