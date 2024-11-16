# Recursão

## O que é Recursão?
Recursão é uma técnica de programação onde uma função chama a si mesma para resolver um problema. Geralmente, um problema maior é dividido em subproblemas menores e mais simples, até que um caso base (ou caso terminal) seja alcançado.

### Estrutura Básica de uma Função Recursiva:
1. **Caso Base:** O ponto de parada da recursão, que define quando a função deve parar de se chamar.
2. **Chamada Recursiva:** A função chama a si mesma com argumentos que a aproximam do caso base.

Exemplo simples de uma função recursiva para calcular o fatorial de um número (\( n! \)):

```python
def fatorial(n):
    if n == 0:  # Caso base
        return 1
    else:
        return n * fatorial(n - 1)  # Chamada recursiva
``` 

# Vantagens da Recursão

## Simplicidade
Alguns problemas, como navegação em árvores ou cálculo de fatorial, podem ser mais intuitivamente resolvidos com recursão.

## Divisão de Problemas
Facilita a quebra de problemas complexos em partes menores e mais gerenciáveis.


# Cuidados ao Usar Recursão

Embora poderosa, a recursão pode causar problemas se não for bem implementada:

## Loop Eterno
Se a função recursiva não possui um caso base claro ou o caso base nunca é atingido, ela entra em um loop eterno. Isso pode levar a um estouro de pilha (_stack overflow_), onde o programa esgota a memória disponível para chamadas de função.

### Exemplo de Loop Eterno
```python
def infinito(n):
    return infinito(n - 1)  # Não há caso base
```

---

# Conceito de Pilhas

Uma **pilha** (ou *stack*, em inglês) é uma estrutura de dados que segue o princípio **LIFO** (Last In, First Out), ou seja, o último elemento a ser inserido é o primeiro a ser removido. Isso significa que o último item adicionado à pilha será o primeiro a ser retirado.

## Como Funciona uma Pilha?

Imagine que você tenha uma lista de afazeres, onde cada tarefa que você adiciona vai para o topo da pilha e, quando a tarefa é concluída, você a remove do topo. Esse processo é o que caracteriza a pilha: só é possível acessar ou remover o item que está no topo, e sempre que um novo item é adicionado, ele fica no topo da pilha.

### Exemplo com Lista de Afazeres

1. **Adicionar Tarefa**: Você tem uma lista de tarefas e começa a adicionar novas atividades. Cada tarefa adicionada vai para o topo da pilha.
2. **Remover Tarefa**: Quando você conclui uma tarefa, você a remove, ou seja, o item no topo é retirado da pilha.

### Exemplo Visual

- **Pilha Inicial**:  
  `[]` (Vazia)

- **Adicionar "Estudar para a prova"**:  
  `[Estudar para a prova]`

- **Adicionar "Comprar mantimentos"**:  
  `[Comprar mantimentos, Estudar para a prova]`

- **Adicionar "Responder e-mails"**:  
  `[Responder e-mails, Comprar mantimentos, Estudar para a prova]`

- **Remover Tarefa**: Quando você termina de responder os e-mails, remove essa tarefa do topo da pilha.  
  `[Comprar mantimentos, Estudar para a prova]` (A tarefa "Responder e-mails" foi removida)

- **Adicionar "Ir à academia"**:  
  `[Ir à academia, Comprar mantimentos, Estudar para a prova]`

Neste exemplo, "Ir à academia" se torna a nova tarefa no topo da pilha, e a próxima tarefa a ser removida será sempre a que está no topo.

## Operações Básicas de uma Pilha

- **Push**: Adiciona um item no topo da pilha.
- **Pop**: Remove o item do topo da pilha.
- **Peek**: Olha o item no topo da pilha sem removê-lo.

## Pilha na Prática

As pilhas são úteis em diversos cenários, como:

- **Controle de chamadas de função**: Em programação, as pilhas são usadas para armazenar o histórico de chamadas de funções. Quando uma função é chamada, ela é empilhada, e quando a função termina, ela é removida da pilha.
- **Desfazer/Refazer**: Em editores de texto, a funcionalidade de desfazer/refazer utiliza pilhas para armazenar as ações realizadas e permitir que o usuário desfaça ou refaça as alterações.


# Resumo

Uma pilha é uma estrutura de dados que segue a ordem **LIFO**, onde o último item adicionado é o primeiro a ser removido. O exemplo da lista de afazeres ajuda a entender como as pilhas funcionam, onde tarefas são adicionadas no topo e removidas à medida que são concluídas.

---

# Recursão e Pilhas Somadas: Busca de uma Chave em Caixas

## O Problema

Imagine que você tem uma grande caixa que contém várias pequenas caixas, e dentro de algumas dessas pequenas caixas podem existir ainda mais caixas. Em uma dessas caixas menores está a chave que você procura. Precisamos usar recursão para procurar a chave, e as pilhas somadas ajudam a organizar as chamadas recursivas durante a busca.

## Como Funciona a Recursão?

A recursão explora as caixas uma por uma. Quando uma caixa contém outras caixas dentro dela, a função se chama novamente para explorar essas caixas menores, empilhando a busca. Cada chamada recursiva representa uma "pilha" de buscas, e ao encontrar a chave, a função começa a retornar, "desempilhando" as buscas anteriores.

## Como Funciona a Pilha de Chamadas?

Cada vez que você entra em uma caixa dentro de outra, uma nova chamada recursiva é feita, e essa chamada adiciona um novo nível à pilha de chamadas. Quando a chave é encontrada, a busca "desempilha" as chamadas anteriores, retornando para os níveis mais altos.

## Exemplo de Código

Imaginemos que temos um conjunto de caixas representado por uma estrutura de lista. Cada caixa pode conter outras caixas (ou estar vazia). Vamos usar recursão para procurar a chave.

```python
def encontrar_chave(caixas):
    # Caso base: Se não há mais caixas para explorar, retorne False
    if not caixas:
        return False
    
    # Percorrendo todas as caixas na lista
    for caixa in caixas:
        if isinstance(caixa, list):  # Se a caixa contém mais caixas (ou seja, é uma lista)
            # Chamada recursiva para explorar as caixas dentro da caixa
            if encontrar_chave(caixa):
                return True
        elif caixa == 'chave':  # Se a caixa contém a chave
            return True
    
    return False
```
# Exemplo de caixas (algumas contêm mais caixas, outras não)
caixas = [
    "livros", 
    ["papéis", "chave"],  # A chave está dentro de uma caixa
    "roupas", 
    ["eletrônicos", ["joias", "chave"]],  # A chave está dentro de uma caixa mais profunda
    "móveis"
]

# Executando a busca
print(encontrar_chave(caixas))  # Deve retornar True, pois a chave está em uma das caixas

## Como as Pilhas Somadas Ajudam

Em cada chamada recursiva, a função armazena informações sobre qual caixa está sendo explorada. Isso é como uma pilha de chamadas: à medida que você entra em caixas mais profundas, você adiciona um novo nível à pilha de buscas. Quando encontra a chave, a pilha começa a ser "desempilhada", retornando para o nível superior, até que a busca termine.

## Resumo

- **Recursão**: Permite explorar caixas dentro de caixas, resolvendo o problema de busca de forma elegante. Cada chamada recursiva explora um nível mais profundo da estrutura de caixas.
- **Pilha**: À medida que a recursão entra nas caixas mais profundas, cada chamada recursiva é empilhada, e a pilha começa a ser "desempilhada" quando a chave é encontrada, ou quando todas as caixas forem exploradas.

Esse processo é uma maneira eficiente de organizar buscas em estruturas hierárquicas como caixas dentro de outras caixas, utilizando recursão e pilhas somadas.
