# Algoritmo de Dijkstra

O algoritmo de Dijkstra é usado para encontrar o caminho mais curto entre vértices em um grafo. Ele é amplamente aplicado em redes de computadores, navegação GPS, sistemas de transporte e outros cenários. A seguir, explicamos os principais conceitos relacionados.


## **Conceitos e Terminologia**

1. **Grafo**: Um conjunto de vértices (ou nós) conectados por arestas (ou arcos).
   - **Vértices**: Representam pontos, como cidades ou computadores.
   - **Arestas**: Conexões entre os vértices, que podem ter **peso**.

2. **Peso**: Cada aresta pode ter um valor associado, representando o custo, distância ou tempo necessário para atravessá-la. Exemplos:
   - Uma aresta com peso `5` pode significar uma estrada de 5 km.
   - Se todas as arestas têm o mesmo peso (ou nenhum), o grafo é considerado **não ponderado**.

3. **Grafo Ponderado e Não Ponderado**:
   - **Ponderado**: As arestas têm valores (pesos).
   - **Não Ponderado**: Todas as arestas têm o mesmo peso implícito (ex.: `1`).

4. **Ciclo**: Um ciclo ocorre quando é possível começar em um vértice, seguir arestas e retornar ao mesmo vértice sem repetir arestas.
   - **Grafo não direcionado**: Se houver um ciclo, ele será bidirecional.
   - **Ciclo e eficiência**: Passar mais de uma vez por um ciclo nunca será mais rápido, já que repetir caminhos aumenta o custo total.

5. **Caminho mais curto**: A rota que conecta dois vértices com o menor peso total.


## **O Problema dos Ciclos**

- Se um grafo tem um ciclo e você continua circulando por ele, o custo só aumenta.
- O algoritmo de Dijkstra evita ciclos ao selecionar sempre o caminho com menor custo acumulado. Uma vez que o caminho mais curto para um vértice é confirmado, ele não é revisitado.


## **Arestas com Pesos Negativos**

- Pesos negativos são problemáticos para o algoritmo de Dijkstra, pois ele presume que adicionar mais arestas nunca diminui o custo total. Isso pode causar erros na determinação do caminho mais curto.
- Para lidar com pesos negativos, utilizamos o **algoritmo de Bellman-Ford**. Ele verifica todos os caminhos possíveis, garantindo a solução correta mesmo com pesos negativos. Além disso, o Bellman-Ford detecta ciclos com peso negativo (onde o custo total diminui a cada ciclo).


## **Exemplo Didático**

Imagine um mapa com cidades conectadas por estradas:
- As cidades são os **vértices**.
- As estradas são as **arestas**, com pesos representando a distância.

Se você deseja viajar da cidade `A` para a cidade `D` com o menor custo:
1. O algoritmo de Dijkstra escolhe sempre a cidade mais próxima ainda não visitada.
2. Ele atualiza o custo total de cada rota até os destinos conectados.
3. O ciclo (por exemplo, `A → B → C → A`) é ignorado, pois revisitar o ciclo aumentaria o custo.

