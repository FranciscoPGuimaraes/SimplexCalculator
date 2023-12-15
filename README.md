# Calculadora Simplex

Este script em Python implementa o método Simplex para resolver problemas de programação linear (PPL). O script recebe um problema de programação linear na forma padrão como entrada e aplica o algoritmo Simplex para encontrar a solução ótima.

## Contribuidores
- Francisco P. Guimarães
- Laura Pivoto Ambrósio
- Rodrigo Paiva Oliveira (Zenks)

## Uso
1. Execute o script em um ambiente Python.
2. Insira o número de variáveis e restrições conforme solicitado.
3. Insira os coeficientes da função objetivo (lucro).
4. Insira os coeficientes das variáveis e restrições, especificando o tipo de restrição (<= ou >=).
5. Insira os coeficientes das constantes nas restrições.

## Observação
- O script assume que o problema de programação linear de entrada está na forma padrão e ignora a restrição de não-negatividade.

## Dependências
- NumPy: `pip install numpy`
- Tabulate: `pip install tabulate`

## Exemplo
Suponha que você tenha o seguinte problema de programação linear:
-Maximizar Z = 3x1 + 2x2
-Sujeito a:
-2x1 + x2 <= 10
-4x1 - 5x2 >= -8
-x1, x2 >= 0

1. Insira o número de variáveis: 2
2. Insira o número de restrições: 2
3. Insira os coeficientes de lucro: 3 2
4. Insira os coeficientes das variáveis para a restrição 1: 2 1
   Insira o tipo de restrição (0 para <=, 1 para >=): 0
5. Insira os coeficientes das variáveis para a restrição 2: 4 -5
   Insira o tipo de restrição (0 para <=, 1 para >=): 1
6. Insira os coeficientes das constantes nas restrições: 10 -8

O script exibirá as matrizes intermediárias e os resultados finais, incluindo o lucro ótimo, os valores ótimos das variáveis e os preços sombra das restrições.

**Observação:** Certifique-se de que NumPy e Tabulate estão instalados em seu ambiente Python antes de executar o script.
