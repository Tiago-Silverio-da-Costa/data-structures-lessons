# Ordenação por seleção(Selection Sort)

## Diferença entre Linked Lists e Arrays em relação ao Big O

## Arrays
Um **array** é uma estrutura de dados onde os elementos estão armazenados em posições contíguas na memória, permitindo acesso direto pelo índice.

### Operações em Arrays:
- **Leitura (\( O(1) \)):** É eficiente, pois os elementos podem ser acessados diretamente pelo índice.
- **Inserção (\( O(n) \)):** Inserir no meio ou no início exige mover os elementos subsequentes para abrir espaço, tornando a operação proporcional ao número de elementos.
- **Deleção (\( O(n) \)):** Remover do meio ou início exige deslocar os elementos para preencher o espaço, também proporcional ao número de elementos.



## Linked Lists
Uma **linked list** é uma estrutura de dados composta por nós, onde cada nó contém um valor e um ponteiro para o próximo nó.

### Operações em Linked Lists:
- **Leitura (\( O(n) \)):** Para acessar um elemento, é necessário percorrer a lista a partir do início até o nó desejado, o que pode ser demorado.
- **Inserção (\( O(1) \)):** Inserir um elemento é rápido, pois basta ajustar os ponteiros (desde que já se saiba onde inserir).
- **Deleção (\( O(1) \)):** Remover um elemento também é eficiente, pois basta ajustar os ponteiros (desde que o nó a ser deletado seja conhecido).

## Tipos de Acesso
Existem dois tipos principais de acesso a elementos em estruturas de dados:

1. **Acesso Aleatório:** Permite acessar diretamente qualquer elemento, dado seu índice. Este tipo de acesso é suportado por **arrays**, pois os elementos estão armazenados em posições contíguas na memória.
2. **Acesso Sequencial:** Os elementos só podem ser acessados percorrendo a estrutura de forma ordenada, começando do início. Este tipo de acesso é característico de **linked lists**, pois os elementos não estão em posições contíguas e dependem de ponteiros para localizar o próximo nó.

## Comparação Geral

| Operação     | Arrays         | Linked Lists   |
|--------------|----------------|----------------|
| **Leitura**  | \( O(1) \)     | \( O(n) \)     |
| **Inserção** | \( O(n) \)     | \( O(1) \)     |
| **Deleção**  | \( O(n) \)     | \( O(1) \)     |

### Resumo
- Use **arrays** quando o acesso direto aos elementos for importante.
- Use **linked lists** quando inserções e deleções frequentes são necessárias.

---

# Combinação de Arrays e Linked Lists: Um Caso de Uso

## O Problema
1. **Busca no Facebook (Binary Search e acesso aleatório):**
   - Para pesquisar usuários pelo nome, usar um **array ordenado** é ideal, porque:
     - Permite o uso de **Binary Search** (\( O(\log n) \)).
     - Oferece **acesso aleatório** eficiente para leitura (\( O(1) \)).

2. **Inserção de novos usuários (novos logins):**
   - Se usarmos apenas o array:
     - Manter o array ordenado exigiria **deslocar elementos** para inserir o novo nome no lugar correto.
     - Isso torna a inserção \( O(n) \) no pior caso, pois todos os elementos subsequentes precisam ser movidos.


## A Solução Híbrida
Para equilibrar eficiência em busca e inserção, podemos combinar **arrays** e **linked lists**:

- **Array como índice categorizado (26 posições):**
  - Cada posição no array corresponde a uma letra do alfabeto (A-Z).
  - Cada posição armazena uma **linked list** com os nomes que começam com essa letra.

### Como funciona:
1. **Busca:**
   - Identifique a letra inicial do nome (\( O(1) \)).
   - Use uma **linked list** para armazenar os nomes começando com essa letra.
   - Dentro da linked list, percorra os nomes para encontrar o desejado (\( O(k) \), onde \( k \) é o número de nomes na categoria).

2. **Inserção:**
   - Determine a letra inicial do novo nome (\( O(1) \)).
   - Adicione o nome diretamente na linked list correspondente (\( O(1) \) para inserir no início, sem ordenação).

3. **Deleção:**
   - Encontre o nome na linked list correspondente e remova (\( O(k) \)).


## Análise de Velocidade
### Vantagens:
- **Busca:** A categorização reduz o tamanho da pesquisa, pois você só percorre os nomes que começam com uma letra específica (\( O(k) \), com \( k \ll n \), onde \( n \) é o número total de usuários).
- **Inserção:** Inserir um novo nome na linked list de uma categoria é rápido (\( O(1) \)) porque não exige deslocar elementos como em um array puro.
- **Deleção:** Similar à inserção, é mais rápida (\( O(k) \)) do que em arrays, pois não requer deslocamentos.

### Desvantagens:
- A busca dentro de uma categoria ainda exige percorrer a linked list (\( O(k) \)), o que pode ser mais lento do que um array ordenado em \( O(\log k) \).
- Gerenciar linked lists aumenta a complexidade da estrutura e pode usar mais memória devido aos ponteiros.


## Conclusão: É mais rápido?
### Para inserções e deleções:
Sim, é mais rápido. Como as linked lists não exigem deslocamento de elementos, elas têm vantagem sobre arrays puros para essas operações.

### Para buscas:
Depende:
- Se o número de usuários por letra (\( k \)) for pequeno, a pesquisa sequencial na linked list será eficiente.
- Porém, se as categorias forem desbalanceadas (por exemplo, muitos nomes começando com "S"), a eficiência pode cair em relação a um array ordenado, que permite busca binária (\( O(\log n) \)).


## Quando usar a solução híbrida?
- Quando as **inserções** e **deleções** são frequentes e há muitos usuários.
- Quando a busca pode ser segmentada logicamente (como por letra inicial).

Essa abordagem combina o melhor dos dois mundos, mas deve ser usada com cuidado para evitar desbalanceamento nas categorias!

---

# Ordenando Músicas Mais Tocadas em uma Playlist

## O Problema
Imagine que queremos ordenar as músicas de uma playlist com base no número de vezes que cada música foi tocada. A ideia proposta é a seguinte:

1. Percorrer um array com todas as músicas.
2. Comparar o número de reproduções (plays) da música selecionada com as demais músicas no array.
3. Repetir o processo várias vezes até formar um novo array ordenado com as músicas mais tocadas no topo.


## Big O da Solução
### Estrutura do Algoritmo
Esse método corresponde a uma **ordenação por seleção** (Selection Sort) ou algo similar. O algoritmo realiza o seguinte:

1. Para cada música no array, percorre todas as outras músicas para comparar o número de reproduções.
2. Após encontrar a música mais tocada na comparação, adiciona-a ao novo array.

O número de comparações feitas é proporcional ao quadrado do número total de músicas, pois:
- O primeiro loop percorre \( n \) músicas.
- Para cada música, o segundo loop percorre \( n-1 \), \( n-2 \), e assim por diante.

**Tempo de execução total:**  
\[ O(n) + O(n-1) + O(n-2) + \ldots + O(1) = O(n^2) \]


## Análise de Complexidade
- **Pior Caso:** \( O(n^2) \), pois cada música é comparada com todas as outras músicas.
- **Melhor Caso:** Mesmo no caso ideal, a complexidade permanece \( O(n^2) \), pois o algoritmo compara todos os elementos para garantir a ordenação.


## Por que \( O(n^2) \)?
O \( O(n^2) \) surge porque:
1. Cada música no array é comparada com as outras músicas \( n-1 \) vezes.
2. Esse número de comparações cresce exponencialmente à medida que o número de músicas aumenta.

## Resumo
Ordenar músicas mais tocadas utilizando essa abordagem leva a uma complexidade \( O(n^2) \), o que é aceitável para listas pequenas, mas pode ser ineficiente para playlists com muitas músicas. Para melhorar, seria interessante usar algoritmos de ordenação mais eficientes, como **Quick Sort** ou **Merge Sort**, que possuem complexidade \( O(n \log n) \).
