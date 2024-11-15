# Introdução à Pesquisa Binária e Notação Big O

Neste capítulo introdutório, falamos sobre **pesquisa binária** (*binary search*), um conceito que nos leva a pensar em uma abordagem eficiente para resolver problemas de busca. Imagine um cenário simples em que precisamos adivinhar um número que uma pessoa está pensando, dentro do intervalo de 1 a 100.

Se usássemos uma abordagem de pesquisa simples (ou "ingênua"), teríamos que percorrer todos os números, um por um, até encontrar o número escolhido. O diferencial da **pesquisa binária** é que ela divide o problema ao meio a cada tentativa. Por exemplo, começamos perguntando se o número pensado é 50. A pessoa responde se o número é maior, menor ou igual a 50. Com essa informação, eliminamos metade do intervalo de possibilidades.

Se o número for maior que 50, descartamos todos os números de 1 a 50 e seguimos testando, por exemplo, 75. Assim, o intervalo continua sendo reduzido pela metade até encontrarmos o número correto.

## Relacionando com o **Big O**

Um ponto interessante da pesquisa binária é o número máximo de tentativas necessárias para acertar no **pior caso**. Se o intervalo é de 1 a 100, o máximo de tentativas será 7. Por quê? Aqui entra o conceito de **notação Big O**.

A **notação Big O** é uma forma utilizada para descrever o desempenho de um algoritmo de maneira precisa. Ela mede como o tempo de execução de um código cresce com o tamanho da entrada. Há diversos tipos de Big O, que discutiremos mais adiante. Primeiro, vejamos o conceito geral:

- A pesquisa binária utiliza logaritmos na **base 2** para calcular o desempenho. No nosso caso, com 100 elementos, a notação seria **O(log(n))**, onde **n** é o total de elementos. Assim, temos:

O(log(100))≈6,64

Arredondamos para 7, pois as tentativas devem ser inteiras e o número mais próximo ao cálculo é 7.

- Já a pesquisa simples, por comparação, tem um desempenho de **O(n)**, onde **n** é o total de elementos. Nesse caso, no pior cenário, precisaríamos de 100 tentativas para acertar.


## Tipos de Notação Big O

Abaixo, alguns dos tipos mais comuns de notação Big O e exemplos práticos:

- **O(log n)** - Tempo logarítmico. Exemplo: pesquisa binária.
- **O(n)** - Tempo linear. Exemplo: pesquisa simples.
- **O(n \* log n)** - Algoritmos de ordenação eficientes. Exemplo: *quicksort*.
- **O(n²)** - Algoritmos lentos de ordenação. Exemplo: ordenação por seleção.
- **O(n!)** - Algoritmos extremamente lentos. Exemplo: problema do caixeiro-viajante.


# Problema do Caixeiro Viajante (TSP)

O **Problema do Caixeiro Viajante** (*Traveling Salesperson Problem*, ou TSP) é um dos problemas mais conhecidos na ciência da computação e na matemática combinatória. Ele pertence à classe de problemas **NP-difíceis**, o que significa que não existe uma solução eficiente conhecida para resolver todos os casos possíveis.

## O Problema

Imagine um caixeiro viajante que precisa visitar um conjunto de cidades apenas uma vez e retornar à cidade de origem. O objetivo é determinar o caminho mais curto possível que conecte todas as cidades, ou seja, minimizar a distância total percorrida.

### Exemplo:
Dado um conjunto de 5 cidades: A, B, C, D e E, com as distâncias entre elas conhecidas, o caixeiro precisa encontrar a rota mais curta, como por exemplo:
A → C → E → B → D → A

A dificuldade do problema está no fato de que, conforme o número de cidades aumenta, o número de combinações possíveis de rotas cresce **exponencialmente**. Para um total de \( n \) cidades, há \( (n-1)! \) rotas possíveis. Isso ocorre porque:

1. Há \( n! \) maneiras de organizar \( n \) cidades.
2. Como o ponto inicial e final são os mesmos, eliminamos redundâncias dividindo por \( n \), resultando em \( (n-1)! \).

### Exemplos:
- Para 4 cidades: \( (4-1)! = 3! = 6 \) combinações.
- Para 10 cidades: \( (10-1)! = 9! = 362,880 \) combinações.
- Para 20 cidades: \( (20-1)! = 19! = 121,645,100,408,832,000 \) combinações!

Esse crescimento rápido torna inviável resolver o problema exaustivamente (testando todas as combinações) para um grande número de cidades.


# O Que Significa o Símbolo `!` (Fatorial)?

O símbolo `!` é chamado de **fatorial** e é uma operação matemática que significa "o produto de todos os números inteiros positivos de 1 até aquele número". Por exemplo:

\[
n! = n \times (n-1) \times (n-2) \times \cdots \times 1
\]

---

## Exemplo: \( 4! \)
O cálculo de \( 4! \) é:

\[
4! = 4 \times 3 \times 2 \times 1 = 24
\]
