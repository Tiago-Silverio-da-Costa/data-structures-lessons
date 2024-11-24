# Programação Dinâmica: Descrição Detalhada

## O Que é Programação Dinâmica?

Programação dinâmica é uma técnica de otimização utilizada para resolver problemas complexos dividindo-os em subproblemas menores e resolvendo-os apenas uma vez, armazenando os resultados (técnica chamada de **memoização**) para evitar cálculos redundantes.

Ela é especialmente útil em problemas que possuem:

1. **Subproblemas sobrepostos**: O problema pode ser dividido em partes menores, que se repetem em diferentes contextos.
2. **Propriedade de subestrutura ótima**: A solução ótima do problema geral pode ser construída a partir das soluções ótimas dos subproblemas.

## Abordagens

Existem duas abordagens principais em programação dinâmica:

1. **Top-down (Memoização)**:
   - Solução recursiva que armazena os resultados dos subproblemas resolvidos para reutilização futura.
   - Evita o cálculo repetido.
2. **Bottom-up (Tabulação)**:
   - Resolve subproblemas menores primeiro e usa seus resultados para resolver subproblemas maiores.
   - Constrói a solução de forma iterativa, geralmente usando uma tabela.

## Estrutura Geral de Problemas Resolvidos com Programação Dinâmica

1. Identificar o estado do problema.
2. Formular uma relação de recorrência (como o estado atual depende de estados anteriores).
3. Determinar as condições base (casos triviais).
4. Implementar uma abordagem **top-down** ou **bottom-up** para resolver o problema.

## Exemplo 1: Problema do Fibonacci

Queremos calcular o \( n \)-ésimo número de Fibonacci, onde:

- \( F(0) = 0 \)
- \( F(1) = 1 \)
- \( F(n) = F(n-1) + F(n-2) \) para \( n \geq 2 \).

### Solução com Programação Dinâmica (Bottom-up)

Criamos uma tabela para armazenar os valores dos números de Fibonacci.

| \( n \)    | 0   | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   |
| ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| \( F(n) \) | 0   | 1   | 1   | 2   | 3   | 5   | 8   | 13  | 21  |

**Código em Python:**

```python
def fibonacci(n):
    if n <= 1:
        return n
    dp = [0] * (n + 1)
    dp[0] = 0
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]

print(fibonacci(8))  # Saída: 21
```

# Exemplo de Programação Dinâmica com Abordagem Top-Down

## Problema: Fibonacci

Queremos calcular o \( n \)-ésimo número de Fibonacci, onde:

- \( F(0) = 0 \)
- \( F(1) = 1 \)
- \( F(n) = F(n-1) + F(n-2) \) para \( n \geq 2 \).

---

## Solução com Memoização (Top-Down)

### Passos:

1. Criamos um dicionário (\( \text{memo} \)) para armazenar os resultados já calculados.
2. Utilizamos a recursão para resolver o problema.
3. Antes de calcular \( F(n) \), verificamos se o resultado já está armazenado no \( \text{memo} \).
4. Caso contrário, calculamos \( F(n) \), armazenamos no \( \text{memo} \), e retornamos o valor.

### Código:

```python
def fibonacci(n, memo={}):
    # Caso base
    if n <= 1:
        return n

    # Verifica se o valor já foi calculado
    if n in memo:
        return memo[n]

    # Calcula e armazena no memo
    memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)

    return memo[n]

# Exemplo de uso
n = 8
print(f"Fibonacci({n}) = {fibonacci(n)}")  # Saída: Fibonacci(8) = 21
```

---

# Mochila com Programação Dinâmica (Bottom-Up)

## Descrição do Problema

Imagine que você tem uma mochila com capacidade de peso **5 kg**. Você tem 3 itens para escolher, e cada item tem um peso e um valor:

| Item | Peso (kg) | Valor ($) |
| ---- | --------- | --------- |
| 1    | 1         | 6         |
| 2    | 2         | 10        |
| 3    | 3         | 12        |

O objetivo é **maximizar o valor total** dos itens na mochila sem exceder o limite de peso.

## Como Resolver

Vamos usar **Programação Dinâmica** para encontrar a melhor solução. A ideia é criar uma tabela `dp[i][w]`, onde:

- **`i`** representa o número de itens considerados.
- **`w`** representa a capacidade atual da mochila.

O valor em `dp[i][w]` será o **valor máximo possível** considerando os `i` primeiros itens e uma capacidade de `w` kg.

## Passos da Solução

### 1. Definir a Recorrência:

- **Se não incluirmos o item atual:**  
  \[
  dp[i][w] = dp[i-1][w]
  \]  
  (valor máximo sem o item `i`).
- **Se incluirmos o item atual:**  
  \[
  dp[i][w] = dp[i-1]w - peso[i]] + valor[i]
  \]  
  (valor máximo incluindo o item `i`).

- Escolhemos a melhor das duas opções:  
  \[
  dp[i][w] = \max(dp[i-1][w], dp[i-1]w - peso[i]] + valor[i])
  \]

### 2. Condições Iniciais (Base Case):

- **Se não há itens (\( i = 0 \)):**  
  \[
  dp[0][w] = 0 \quad \text{para qualquer \( w \)}.
  \]
- **Se a capacidade é 0 (\( w = 0 \)):**  
  \[
  dp[i][0] = 0 \quad \text{para qualquer \( i \)}.
  \]

### 3. Construir a Tabela:

Usamos iteração para preencher a tabela `dp`, linha por linha.

## Resolvendo o Exemplo

### Tabela Inicial:

| \( i \backslash w \) | 0   | 1   | 2   | 3   | 4   | 5   |
| -------------------- | --- | --- | --- | --- | --- | --- |
| 0 (sem itens)        | 0   | 0   | 0   | 0   | 0   | 0   |

### Iteração 1: Considerando o **Item 1 (Peso = 1, Valor = 6)**:

- Se \( w \geq 1 \), podemos incluir o Item 1.
- Caso contrário, usamos o valor da linha acima.

| \( i \backslash w \) | 0   | 1   | 2   | 3   | 4   | 5   |
| -------------------- | --- | --- | --- | --- | --- | --- |
| 1                    | 0   | 6   | 6   | 6   | 6   | 6   |

### Iteração 2: Considerando o **Item 2 (Peso = 2, Valor = 10)**:

- Se \( w < 2 \), não podemos incluir o Item 2.
- Caso \( w \geq 2 \), escolhemos entre incluir ou não o Item 2.

| \( i \backslash w \) | 0   | 1   | 2   | 3   | 4   | 5   |
| -------------------- | --- | --- | --- | --- | --- | --- |
| 2                    | 0   | 6   | 10  | 16  | 16  | 16  |

### Iteração 3: Considerando o **Item 3 (Peso = 3, Valor = 12)**:

- Se \( w < 3 \), não podemos incluir o Item 3.
- Caso \( w \geq 3 \), escolhemos entre incluir ou não o Item 3.

| \( i \backslash w \) | 0   | 1   | 2   | 3   | 4   | 5   |
| -------------------- | --- | --- | --- | --- | --- | --- |
| 3                    | 0   | 6   | 10  | 16  | 18  | 22  |

## Interpretação da Tabela Final

A última célula da tabela, \( dp[3][5] = 22 \), é a resposta. Isso significa que o **valor máximo** que podemos obter na mochila, considerando os 3 itens e uma capacidade de 5 kg, é **22**.

## Código em Python:

```python
def knapsack(capacity, weights, values, n):
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]

# Dados
weights = [1, 2, 3]
values = [6, 10, 12]
capacity = 5
n = len(weights)

print(knapsack(capacity, weights, values, n))  # Saída: 22
```
