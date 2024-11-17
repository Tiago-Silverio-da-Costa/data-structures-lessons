
# Tabelas Hash

## O que são Tabelas Hash?

Tabelas hash são uma estrutura de dados que permite armazenar e buscar dados de maneira extremamente eficiente. Elas funcionam associando **chaves** a **valores** por meio de uma **função hash**, que transforma a chave em um índice dentro de um array.

No melhor caso, as operações de busca, inserção e remoção têm tempo de execução \(O(1)\), o que significa que o tempo necessário para realizar essas operações é constante, independentemente do tamanho da tabela.


## Funcionamento Básico

1. **Inserção**:
   - A chave é processada pela função hash, gerando um índice.
   - O valor é armazenado na posição correspondente a esse índice.

2. **Busca**:
   - A chave é passada pela função hash para obter o índice.
   - O valor armazenado nesse índice é recuperado.

3. **Remoção**:
   - Localiza-se o índice pela chave, e o valor associado é removido.


## Características do \(O(1)\): Tempo Constante

No caso ideal (sem colisões):
- A função hash transforma a chave diretamente em um índice fixo.
- O valor correspondente pode ser acessado sem a necessidade de percorrer outros elementos, como ocorre em listas.

Isso faz com que tabelas hash combinem:
- A velocidade dos arrays na **busca**.
- A eficiência das listas na **inserção** e **remoção**.

Por isso, as tabelas hash são consideradas o "melhor dos dois mundos". No entanto, no **pior caso** (quando há muitas colisões), tabelas hash podem ser lentas em ambas as operações, o que deve ser evitado.


## Colisões: O Que São e Como Lidar

### O que é uma Colisão?

Uma colisão ocorre quando duas ou mais chaves diferentes geram o mesmo índice pela função hash. Isso acontece porque:
1. O tamanho da tabela (array) é limitado, enquanto o número de possíveis chaves é potencialmente infinito.
2. A função hash pode gerar o mesmo índice para diferentes chaves.

### Impacto das Colisões

- Quando há colisões, o desempenho das tabelas hash pode degradar-se.
- Em alguns casos, a busca, inserção e remoção passam a ter complexidade \(O(n)\), onde \(n\) é o número de elementos armazenados.

### Estratégias para Resolver Colisões

1. **Encadeamento (Chaining)**:
   - Cada índice da tabela aponta para uma lista que armazena os valores que colidiram.
   - Exemplo:
     - Índice 3: [("Ana", 123), ("Bob", 456)]
   - **Prós**: Fácil de implementar e sem limite de elementos por índice.
   - **Contras**: Se as listas forem muito longas, o desempenho diminui.

2. **Endereçamento Aberto (Open Addressing)**:
   - Ao invés de usar listas, procura-se outro índice vazio na tabela.
   - Técnicas:
     - **Linear probing**: Procura sequencialmente.
     - **Quadratic probing**: Procura de forma quadrática.
     - **Double hashing**: Usa uma segunda função hash.
   - **Prós**: Reduz o uso de memória extra.
   - **Contras**: Pode causar **clusters**, dificultando as buscas.


## Prevenindo Colisões

Para evitar colisões e manter um bom desempenho:
1. **Use uma boa função hash**:
   - Deve mapear as chaves uniformemente por toda a tabela.
   - Deve minimizar colisões.
2. **Mantenha um baixo fator de carga**:
   - O fator de carga é a relação entre o número de elementos na tabela e seu tamanho.
   - Tabelas muito cheias aumentam o risco de colisões. A solução é redimensionar a tabela.


## Importância da Função Hash

A função hash é essencial para o bom desempenho das tabelas hash. Ela deve:
- Mapear todas as chaves para um único espaço.
- Distribuir as chaves de maneira simétrica por toda a tabela.

Uma boa função hash reduz a probabilidade de colisões e mantém as listas encadeadas curtas, garantindo eficiência.


## O "Melhor dos Dois Mundos" e o Pior Caso

- **Vantagens**:
  - As tabelas hash são tão rápidas quanto arrays na busca.
  - São tão eficientes quanto listas na inserção e remoção.
  - Essa combinação faz delas uma solução ideal para muitos problemas.

- **O Pior Caso**:
  - No pior cenário (muitas colisões), tabelas hash se tornam lentas tanto na busca quanto na inserção e remoção.
  - Para evitar esse caso:
    1. Use uma **boa função hash**.
    2. Mantenha um **baixo fator de carga**.


## Resumo: Vantagens e Desvantagens

### Vantagens
- Busca rápida, semelhante a arrays.
- Inserção e remoção eficientes, como listas.
- Versátil e fácil de implementar.

### Desvantagens
- Pode consumir mais memória.
- O desempenho depende da função hash e da gestão de colisões.
- No pior caso, a eficiência é reduzida.

---

# Comparação de Complexidade (Big O) entre Arrays, Listas Ligadas e Tabelas Hash

| Operação         | **Array**           | **Lista Ligada**     | **Tabela Hash**       |
|-------------------|---------------------|-----------------------|-----------------------|
| **Acesso Direto** | \(O(1)\)            | \(O(n)\)             | \(O(1)\) (melhor caso) |
| **Busca**         | \(O(n)\)            | \(O(n)\)             | \(O(1)\) (melhor caso), \(O(n)\) (pior caso) |
| **Inserção**      | \(O(n)\) ou \(O(1)\)* | \(O(1)\)             | \(O(1)\) (melhor caso), \(O(n)\) (pior caso) |
| **Remoção**       | \(O(n)\)            | \(O(1)\)             | \(O(1)\) (melhor caso), \(O(n)\) (pior caso) |


## Explicações

### 1. **Acesso Direto**
- **Array**: O acesso direto é rápido (\(O(1)\)) porque os elementos estão armazenados em posições contíguas de memória.
- **Lista Ligada**: É necessário percorrer os elementos para encontrar a posição desejada (\(O(n)\)).
- **Tabela Hash**: O acesso depende da função hash, que no melhor caso é \(O(1)\).


### 2. **Busca**
- **Array** e **Lista Ligada**: É necessário percorrer os elementos (\(O(n)\)) no pior caso.
- **Tabela Hash**: A busca é \(O(1)\) no melhor caso, mas pode ser \(O(n)\) no pior caso devido a colisões.


### 3. **Inserção**
- **Array**:
  - \(O(1)\): Ao adicionar no final (se houver espaço).
  - \(O(n)\): Ao inserir em uma posição específica, pois os elementos precisam ser deslocados.
- **Lista Ligada**: A inserção é \(O(1)\) ao adicionar no início ou no final (se a posição for conhecida).
- **Tabela Hash**: A inserção é \(O(1)\) no melhor caso, mas pode ser \(O(n)\) em caso de colisões e encadeamento longo.


### 4. **Remoção**
- **Array**: A remoção exige deslocamento dos elementos (\(O(n)\)).
- **Lista Ligada**: A remoção é \(O(1)\) se a posição for conhecida (ajuste dos ponteiros).
- **Tabela Hash**: A remoção é \(O(1)\) no melhor caso, mas pode ser \(O(n)\) no pior caso devido a colisões.


\* Inserção em arrays pode ser \(O(1)\) apenas quando o elemento é adicionado no final e não há necessidade de realocar o array.



