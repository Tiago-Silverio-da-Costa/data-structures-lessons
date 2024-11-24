# Algoritmos Gulosos (Greedy)

## Conceito
Algoritmos gulosos são uma abordagem para resolver problemas de otimização, onde o objetivo é encontrar a melhor solução possível (ótima ou aproximada) seguindo um processo iterativo que faz escolhas locais ótimas a cada etapa, na esperança de que essas escolhas levem a uma solução global ótima.

### Características dos Algoritmos Gulosos
1. **Escolhas Locais Ótimas**:
   - A cada etapa, o algoritmo escolhe a melhor opção disponível naquele momento sem considerar o impacto dessa escolha no futuro.
   
2. **Irrevogabilidade**:
   - Uma vez tomada uma decisão, ela não pode ser desfeita ou revisada.

3. **Problemas adequados**:
   - Algoritmos gulosos são aplicáveis apenas quando o problema possui a *Propriedade da Escolha Gulosa* e a *Subestrutura Ótima* (explicados abaixo).

### Propriedade da Escolha Gulosa
- Significa que uma solução ótima global pode ser alcançada fazendo escolhas locais ótimas em cada etapa do processo.
- Em outras palavras, decidir a melhor solução parcial em uma etapa não compromete a capacidade de encontrar a solução ótima final.

### Subestrutura Ótima
- Um problema tem subestrutura ótima se a solução ótima para o problema completo pode ser construída a partir de soluções ótimas de seus subproblemas.


## Exemplo de Aplicação: Problema da Cobertura de Conjuntos
O problema da cobertura de conjuntos (*Set Cover Problem*) é um problema clássico onde o objetivo é escolher o menor número de conjuntos que cobrem todos os elementos de um universo.

### Definição Formal
1. **Dado**:
   - Um conjunto universo \( U \) de elementos.
   - Uma coleção de subconjuntos \( S_1, S_2, \ldots, S_n \), onde cada \( S_i \subseteq U \).
2. **Objetivo**:
   - Encontrar um subconjunto mínimo de \( S_1, S_2, \ldots, S_n \) tal que a união desses conjuntos cubra todos os elementos de \( U \).

### Estratégia Gulosa
- A cada iteração, escolha o conjunto \( S_i \) que cobre o maior número de elementos não cobertos no momento.
- Continue até que todos os elementos do universo estejam cobertos.


## Exemplo Didático
### Dados:
- Universo \( U = \{1, 2, 3, 4, 5\} \)
- Conjuntos:
  - \( S_1 = \{1, 2, 3\} \)
  - \( S_2 = \{2, 4\} \)
  - \( S_3 = \{3, 4, 5\} \)

### Passo a Passo:
1. **Inicialmente**:
   - \( U = \{1, 2, 3, 4, 5\} \).
2. Escolha \( S_1 \) porque cobre 3 elementos (\( \{1, 2, 3\} \)).
   - Elementos restantes: \( \{4, 5\} \).
3. Escolha \( S_3 \) porque cobre 2 elementos (\( \{4, 5\} \)).
   - Elementos restantes: \( \emptyset \) (todos cobertos).
4. **Solução**:
   - \( \{S_1, S_3\} \).


## Vantagens dos Algoritmos Gulosos
1. **Eficiência**:
   - Muitas vezes são rápidos e fáceis de implementar.
2. **Simplicidade**:
   - Não requerem cálculos complexos ou abordagens como programação dinâmica.


## Limitações
1. **Nem sempre encontra a solução ótima**:
   - Alguns problemas exigem reavaliações ou escolhas futuras, o que os gulosos ignoram.
   - Exemplo: O problema da mochila (*Knapsack Problem*) com itens divisíveis tem solução ótima com algoritmo guloso, mas o caso de itens indivisíveis requer abordagem diferente.
   
2. **Dependência da propriedade gulosa**:
   - Se o problema não possuir essa propriedade, a abordagem gulosa pode falhar.


## Resumo
- Algoritmos gulosos funcionam bem para problemas com subestrutura ótima e escolha gulosa.
- São úteis para problemas como:
  - Cobertura de conjuntos,
  - Caminho mínimo (algoritmo de Dijkstra),
  - Problema do troco (com moedas de valores específicos).
- É importante analisar se a solução gulosa é válida para o problema antes de aplicá-la.

---

# Para cada um desses algoritmos, diga se ele é um algoritmo guloso ou não:
a. Quicksort  
b. Pesquisa em Largura (BFS)  
c. Algoritmo de Dijkstra  


## Respostas

### **a. Quicksort**
- **Não é um algoritmo guloso.**
  - **Por quê?**
    - O Quicksort é um algoritmo de ordenação que utiliza a estratégia de *Divisão e Conquista*. Ele divide os dados em subproblemas (com base em um pivô) e resolve esses subproblemas recursivamente, mas não toma decisões baseadas em escolhas locais ótimas para alcançar a solução global. 
    - Embora escolha um pivô, essa escolha não é relacionada à otimização de uma solução global; é apenas uma parte do processo de particionamento.


### **b. Pesquisa em Largura (BFS)**
- **Não é um algoritmo guloso.**
  - **Por quê?**
    - O algoritmo de pesquisa em largura (BFS) é usado para explorar grafos de forma sistemática, camada por camada, utilizando uma fila. Ele não faz escolhas baseadas em ganhos imediatos ou decisões ótimas em cada etapa, mas segue um processo de exploração uniforme para garantir que todos os caminhos de um determinado nível sejam explorados antes de passar para o próximo.


### **c. Algoritmo de Dijkstra**
- **Sim, é um algoritmo guloso.**
  - **Por quê?**
    - O algoritmo de Dijkstra utiliza a abordagem gulosa para encontrar o caminho mais curto de um vértice inicial a todos os outros em um grafo ponderado. Ele sempre escolhe o próximo vértice com a menor distância acumulada (localmente ótimo) na esperança de que essa escolha leve à solução global ótima.
    - A propriedade gulosa é válida porque o problema do caminho mínimo possui subestrutura ótima, garantindo que a solução local leve à solução global correta.

---

# Algoritmos Gulosos e Problemas NP-Completos

## O Que é NP-Completo?
- **NP (Nondeterministic Polynomial time)**: Refere-se ao conjunto de problemas que podem ser verificados (ou solucionados) por uma máquina de Turing não-determinística em tempo polinomial.
- **Problemas NP-Completos** são um subconjunto de problemas NP que possuem as seguintes propriedades:
  1. **Estão em NP**:
     - Isso significa que, dada uma solução para o problema, é possível verificar sua correção em tempo polinomial.
  2. **São NP-difíceis**:
     - Qualquer outro problema em NP pode ser reduzido a esse problema em tempo polinomial.

Em termos simples, resolver um problema NP-completo eficientemente significaria resolver todos os problemas em NP com eficiência.

# O Que é Tempo Polinomial?

## Definição
Tempo polinomial refere-se ao tempo de execução de um algoritmo que pode ser expressado como uma função polinomial do tamanho da entrada. Em termos mais simples, se o tempo de execução de um algoritmo é proporcional a \( n^k \), onde:
- \( n \) é o tamanho da entrada,
- \( k \) é uma constante fixa,

então o algoritmo é considerado eficiente e dito que opera em **tempo polinomial**.
---

## Exemplos de Funções Polinomiais
- \( n \)
- \( n^2 \)
- \( n^3 \)
- \( 5n^4 + 3n^2 + 7 \)

Todas essas funções crescem de maneira polinomial. Embora o crescimento possa ser rápido para \( k \) grandes, elas ainda são consideradas gerenciáveis em comparação com funções que crescem mais rápido, como exponenciais.


## Tempo Polinomial vs Outros Tipos de Crescimento
1. **Polinomial (\( n^k \))**:
   - Exemplos:
     - \( n \), \( n^2 \), \( n^3 \)
     - Cresce relativamente devagar.
   - **Exemplo prático**:
     - Ordenação por inserção (\( n^2 \)).
   
2. **Exponencial (\( 2^n \))**:
   - Cresce muito rapidamente e é impraticável para entradas grandes.
   - **Exemplo prático**:
     - Resolver o problema do Caixeiro Viajante por força bruta (\( n! \)).
   
3. **Logarítmico (\( \log(n) \))**:
   - Cresce muito lentamente.
   - **Exemplo prático**:
     - Pesquisa binária (\( \log(n) \)).

4. **Fatorial (\( n! \))**:
   - Crescimento extremamente rápido.
   - **Exemplo prático**:
     - Gerar todas as permutações possíveis de \( n \) elementos.


## Importância do Tempo Polinomial
- **Classificação de Problemas Computacionais**:
  - Problemas que podem ser resolvidos em tempo polinomial pertencem à classe **P** (*polynomial time*), considerada a classe dos problemas "fáceis" ou "tratáveis".
  - Problemas fora de P, como aqueles em NP, muitas vezes não possuem algoritmos conhecidos que os resolvam em tempo polinomial.

- **Eficiência Prática**:
  - Algoritmos que operam em tempo polinomial são geralmente preferidos porque escalam melhor para entradas grandes.


## Exemplo de Algoritmos em Tempo Polinomial
1. **Ordenação por Inserção**:
   - Complexidade: \( O(n^2) \).
   - Explicação: O número de comparações feitas cresce com o quadrado do tamanho da entrada.

2. **Pesquisa Linear**:
   - Complexidade: \( O(n) \).
   - Explicação: O tempo de execução cresce linearmente com o número de elementos.

3. **Busca em Largura (BFS)**:
   - Complexidade: \( O(V + E) \), onde \( V \) é o número de vértices e \( E \) é o número de arestas.


## Conclusão
Tempo polinomial é uma métrica fundamental para avaliar a eficiência dos algoritmos. Algoritmos em tempo polinomial são práticos para a maioria das aplicações, enquanto tempos de execução exponenciais ou fatoriais frequentemente tornam algoritmos inviáveis para entradas maiores.

## Como Identificar se um Problema é NP-Completo?

### 1. **Pertence à Classe NP**
   - Primeiro, verifique se o problema pode ser verificado em tempo polinomial.
   - **Exemplo**:
     - No problema do *Conjunto Independente Máximo*, dado um conjunto de vértices, é possível verificar rapidamente se eles formam um conjunto independente (nenhuma aresta conecta dois vértices do conjunto).

### 2. **Redução Polinomial**
   - Demonstrar que um problema conhecido como NP-completo pode ser transformado no problema em questão em tempo polinomial.
   - **Por quê?**
     - Isso indica que o problema é, no mínimo, tão difícil quanto o problema NP-completo usado na redução.
   - **Exemplo**:
     - No problema do Caixeiro Viajante (*Traveling Salesman Problem*), pode-se mostrar que ele é pelo menos tão difícil quanto o problema do Caminho Hamiltoniano, que é conhecido por ser NP-completo.

### 3. **Decisão versus Otimização**
   - Muitos problemas NP-completos são apresentados como problemas de decisão:
     - Por exemplo, no problema da Mochila (*Knapsack Problem*), a versão NP-completa pergunta: "Existe uma combinação de itens que encha a mochila exatamente até \( C \)?"
   - Se a versão de decisão do problema for NP-completa, a versão de otimização associada também é, em geral, NP-difícil.

### 4. **Estrutura Combinatória**
   - Problemas NP-completos geralmente envolvem uma busca combinatória muito grande:
     - Por exemplo, testar todas as permutações possíveis no Caixeiro Viajante ou todas as combinações de subconjuntos no problema da Cobertura de Conjuntos.


## Exemplos de Problemas NP-Completos
1. **Problema do Caixeiro Viajante (TSP)**:
   - Dado um conjunto de cidades e distâncias entre elas, determinar se existe um percurso que passe por todas as cidades uma única vez com um custo menor ou igual a um valor \( k \).

2. **Problema da Mochila (versão de decisão)**:
   - Dado um conjunto de itens com pesos e valores, determinar se é possível selecionar itens que não excedam o peso máximo \( W \) enquanto atingem um valor mínimo \( V \).

3. **Coloração de Grafos**:
   - Dado um grafo, determinar se é possível colori-lo com \( k \) cores de modo que vértices adjacentes tenham cores diferentes.


## Relacionamento com Algoritmos Gulosos
- Muitos problemas NP-completos **não podem ser resolvidos por algoritmos gulosos** de forma eficiente.
  - Isso ocorre porque os algoritmos gulosos dependem de escolhas locais ótimas que, para problemas NP-completos, não garantem a solução global ótima.

### Exemplo: Problema da Mochila
- Um algoritmo guloso que sempre escolhe o item com maior valor/peso pode falhar:
  - Suponha:
    - Item A: peso = 10, valor = 60.
    - Item B: peso = 20, valor = 100.
    - Capacidade = 20.
  - O algoritmo guloso escolheria o item A, deixando de perceber que o item B tem um valor total maior.


## Como Resolver Problemas NP-Completos?
1. **Aproximação**:
   - Desenvolver algoritmos que encontram soluções próximas da ótima em tempo polinomial.
   - Exemplo: Algoritmos gulosos frequentemente são usados para encontrar aproximações.

2. **Força Bruta**:
   - Explorar todas as combinações possíveis (não prático para grandes instâncias).

3. **Programação Dinâmica**:
   - Resolver subproblemas menores e reutilizar soluções para reduzir redundâncias.

4. **Heurísticas**:
   - Algoritmos como *simulated annealing* ou *algoritmos genéticos* podem fornecer soluções aceitáveis para grandes instâncias.

5. **Reduzir o Tamanho do Problema**:
   - Técnicas como poda alfa-beta podem ajudar a limitar o espaço de busca.


## Resumo
Problemas NP-completos são desafiadores porque são difíceis de resolver de forma eficiente. Identificá-los envolve verificar se pertencem à classe NP e se podem ser reduzidos de um problema NP-completo conhecido. Embora algoritmos gulosos possam ser úteis para aproximações, raramente são capazes de resolver problemas NP-completos de forma ótima.

---

# Problemas e Classificação como NP-Completos

Abaixo analisaremos cada um dos problemas apresentados, explicando se eles são NP-completos ou não. Quando for o caso, explicaremos o conceito subjacente, como "clique" e coloração de grafos.


## Problema 1: **Um carteiro deve entregar correspondências para vinte casas, e ele deve encontrar a rota mais curta que passe por todas as vinte casas.**

### Análise
- Este problema é equivalente ao **Problema do Caixeiro Viajante (TSP - Traveling Salesman Problem)**.
  - O carteiro precisa encontrar o menor percurso que passe por todas as casas e retorne ao ponto inicial (rota mais curta com visitas únicas a cada casa).

### É NP-completo?
- **Sim, este problema é NP-completo.**
  - **Por quê?**
    - Está em **NP**: Dada uma solução (uma rota específica), é possível verificar em tempo polinomial se essa rota visita todas as casas e tem o menor comprimento.
    - É **NP-difícil**: O TSP é conhecido como NP-completo, e o problema do carteiro é essencialmente a mesma formulação.

### Características do Problema NP-Completo
- Envolve uma busca combinatória (permutações de casas para encontrar a menor rota).
- Não existe solução eficiente conhecida (em tempo polinomial) para o problema geral.


## Problema 2: **Encontrar o maior clique em um conjunto de pessoas (um clique, neste caso, é um grupo de pessoas em que todas se conhecem).**

### O Que é um Clique?
- Um **clique** em um grafo é um subconjunto de vértices onde todos os vértices do subconjunto estão conectados entre si.
  - No contexto de pessoas, representa um grupo onde todas se conhecem.
  - Formalmente, em um grafo \( G = (V, E) \), um clique \( C \subseteq V \) é tal que para qualquer \( u, v \in C \), a aresta \( (u, v) \) pertence a \( E \).

### É NP-completo?
- **Sim, este problema é NP-completo.**
  - **Por quê?**
    - Está em **NP**: Dado um conjunto de pessoas (um subconjunto de vértices), é possível verificar em tempo polinomial se todos os vértices estão conectados.
    - É **NP-difícil**: O problema do clique é um problema clássico em teoria da complexidade, comprovadamente NP-completo.

### Dificuldade
- Para encontrar o maior clique, seria necessário verificar todas as combinações possíveis de subconjuntos, o que torna o problema impraticável para grandes grafos (tempo exponencial).


## Problema 3: **Você está fazendo um mapa dos Estados Unidos e precisa colorir estados adjacentes com cores diferentes. Para isso, não pode haver dois estados adjacentes com a mesma cor.**

### O Problema Subjacente
- Este problema é conhecido como o **Problema de Coloração de Grafos**.
  - Cada estado é representado por um vértice no grafo.
  - Cada fronteira entre estados é representada por uma aresta.
  - O objetivo é atribuir cores aos vértices de tal forma que dois vértices conectados por uma aresta não tenham a mesma cor.

### É NP-completo?
- **Sim, este problema é NP-completo.**
  - **Por quê?**
    - Está em **NP**: Dada uma coloração do grafo (atribuição de cores aos vértices), é possível verificar em tempo polinomial se a coloração é válida (nenhuma aresta conecta dois vértices com a mesma cor).
    - É **NP-difícil**: O problema da coloração de grafos para \( k \) cores (\( k \)-colorabilidade) é um problema clássico em teoria dos grafos e comprovadamente NP-completo para \( k \geq 3 \).

### Observação
- O **Teorema das Quatro Cores** garante que qualquer mapa plano pode ser colorido com no máximo 4 cores, mas encontrar essa coloração mínima para grafos arbitrários é computacionalmente difícil.


## Resumo
| Problema                                                                                               | NP-Completo? | Explicação                                                                                                                      |
|-------------------------------------------------------------------------------------------------------|-------------|----------------------------------------------------------------------------------------------------------------------------------|
| Carteiro deve encontrar a rota mais curta para entregar correspondências (equivalente ao TSP).        | Sim         | O problema é NP-completo, pois envolve encontrar a menor rota em um grafo ponderado, que é um problema clássico em NP.          |
| Encontrar o maior clique em um conjunto de pessoas.                                                   | Sim         | O problema do clique é NP-completo, pois requer verificar combinações de vértices para identificar o maior conjunto conectado.  |
| Colorir estados adjacentes no mapa dos EUA com cores diferentes.                                      | Sim         | É equivalente ao problema de coloração de grafos, que é NP-completo para determinar a \( k \)-colorabilidade (\( k \geq 3 \)). |
