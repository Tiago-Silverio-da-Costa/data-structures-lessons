# K-Vizinhos Mais Próximos (K-Nearest Neighbors, KNN)

## Conceito Geral
O **K-Vizinhos Mais Próximos (K-Nearest Neighbors, KNN)** é um algoritmo simples e eficaz utilizado em **Aprendizado de Máquina (Machine Learning)** para tarefas de **classificação (classification)** e **regressão (regression)**. Ele se baseia no princípio da **proximidade (proximity)**: dados semelhantes tendem a ter comportamentos ou rótulos semelhantes. O KNN funciona comparando a entrada desconhecida com os dados conhecidos e tomando decisões com base nos **K vizinhos mais próximos (K-nearest neighbors)**.


## Como o KNN Funciona?
1. **Definir o Valor de K**:  
   O valor \( K \) representa o número de vizinhos considerados para tomar uma decisão. Por exemplo, se \( K = 3 \), o algoritmo avalia os 3 vizinhos mais próximos para determinar o rótulo ou valor da entrada.

2. **Calcular a Distância (Distance)**:  
   A proximidade entre os dados é determinada por meio de **fórmulas de distância (distance metrics)**. As fórmulas comuns incluem:
   - **Distância Euclidiana (Euclidean Distance)**.
   - **Distância de Manhattan (Manhattan Distance)**.
   - **Distância de Minkowski (Minkowski Distance)**.
   - **Distância Coseno (Cosine Distance)**.

3. **Classificar ou Predizer (Classify or Predict)**:
   - **Classificação (Classification)**: A entrada é atribuída ao grupo mais frequente entre os \( K \) vizinhos (votação da maioria, majority voting).
   - **Regressão (Regression)**: A saída é a média (ou mediana) dos valores dos \( K \) vizinhos.

4. **Resultado Final (Final Result)**:  
   Após a decisão baseada nos vizinhos, o algoritmo retorna o **rótulo (label)** ou o **valor predito (predicted value)**.


## Aplicações do KNN
1. **Classificação (Classification)**:  
   - Diagnóstico médico (ex.: identificar se um tumor é maligno ou benigno).  
   - Reconhecimento de imagem (ex.: classificar objetos em fotos).

2. **Regressão (Regression)**:  
   - Previsão de preços (ex.: prever o preço de uma casa com base nos preços das casas vizinhas).  
   - Estimativa de notas em sistemas de recomendação.


## Cálculo de Distâncias (Distance Calculation)
A distância é a métrica usada para determinar a proximidade entre dois pontos de dados. Aqui estão as fórmulas mais comuns:

### 1. **Distância Euclidiana (Euclidean Distance)**
É a distância "reta" entre dois pontos em um espaço \( n \)-dimensional. É calculada pela fórmula:  
\[
d(p, q) = \sqrt{\sum_{i=1}^{n} (p_i - q_i)^2}
\]
- **Exemplo**:  
  Pontos \( p = (3, 4) \) e \( q = (6, 8) \):  
  \[
  d(p, q) = \sqrt{(6 - 3)^2 + (8 - 4)^2} = \sqrt{3^2 + 4^2} = \sqrt{9 + 16} = 5
  \]

### 2. **Distância de Manhattan (Manhattan Distance)**
É a soma das diferenças absolutas entre as coordenadas dos dois pontos. A fórmula é:  
\[
d(p, q) = \sum_{i=1}^{n} |p_i - q_i|
\]
- **Exemplo**:  
  Pontos \( p = (3, 4) \) e \( q = (6, 8) \):  
  \[
  d(p, q) = |6 - 3| + |8 - 4| = 3 + 4 = 7
  \]

### 3. **Distância de Minkowski (Minkowski Distance)**
Generaliza as distâncias Euclidiana e de Manhattan. A fórmula é:  
\[
d(p, q) = \left(\sum_{i=1}^{n} |p_i - q_i|^p \right)^{1/p}
\]
- Para \( p = 1 \): É equivalente à distância de Manhattan.  
- Para \( p = 2 \): É equivalente à distância Euclidiana.  
- **Exemplo**:  
  Pontos \( p = (3, 4) \) e \( q = (6, 8) \), com \( p = 3 \):  
  \[
  d(p, q) = \left(|6 - 3|^3 + |8 - 4|^3\right)^{1/3} = \left(3^3 + 4^3\right)^{1/3} = \left(27 + 64\right)^{1/3} \approx 4.64
  \]

### 4. **Distância Coseno (Cosine Distance)**
Mede a similaridade do ângulo entre dois vetores, sendo útil para dados em alta dimensionalidade. A fórmula é:  
\[
d(p, q) = 1 - \frac{\sum_{i=1}^{n} p_i \cdot q_i}{\sqrt{\sum_{i=1}^{n} p_i^2} \cdot \sqrt{\sum_{i=1}^{n} q_i^2}}
\]
- **Exemplo**:  
  Vetores \( p = [1, 2, 3] \) e \( q = [4, 5, 6] \):  
  \[
  d(p, q) = 1 - \frac{(1 \cdot 4) + (2 \cdot 5) + (3 \cdot 6)}{\sqrt{1^2 + 2^2 + 3^2} \cdot \sqrt{4^2 + 5^2 + 6^2}}
  \]
  \[
  d(p, q) = 1 - \frac{4 + 10 + 18}{\sqrt{14} \cdot \sqrt{77}} = 1 - \frac{32}{\sqrt{14} \cdot \sqrt{77}} \approx 0.025
  \]


## Classificação com KNN (Classification with KNN)
No contexto de classificação, o KNN identifica a **classe (class)** da entrada com base nos rótulos dos \( K \) vizinhos mais próximos.

- **Exemplo**:  
  Imagine 2 classes de dados (A e B), onde:  
  - Entrada: \((x, y)\).  
  - \( K = 3 \).  
  O algoritmo identifica os 3 pontos mais próximos no espaço e realiza uma votação:
  - Se 2 pontos pertencem à classe A e 1 à classe B, a entrada é classificada como A.


## Regressão com KNN (Regression with KNN)
No contexto de regressão, o KNN prediz um valor contínuo com base nos \( K \) vizinhos mais próximos, tomando a média (ou mediana) de seus valores.

- **Exemplo**:  
  Você quer prever o preço de uma casa com base nas características das casas vizinhas. Para \( K = 3 \), o preço estimado é a média dos preços das 3 casas mais próximas.


## Aprendizado de Máquina e KNN (Machine Learning and KNN)
Embora o KNN seja considerado um método de **aprendizado supervisionado (supervised learning)**, ele é um algoritmo **preguiçoso (lazy)**:
- **Treinamento "zero"**: O KNN não constrói explicitamente um modelo; apenas armazena os dados de treinamento.
- **Complexidade na Predição**: A maior parte do trabalho ocorre durante a predição, pois ele calcula distâncias para todos os pontos do conjunto de treinamento.

### Vantagens:
- Simples e fácil de implementar.  
- Não faz suposições sobre a distribuição dos dados.  

### Desvantagens:
- Lento para grandes conjuntos de dados.  
- Sensível a dados ruidosos e irrelevantes.  
- Requer normalização para variáveis em escalas diferentes.  


## Código Python: Implementando KNN

### Classificação
```python
from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Gerar dados fictícios
X, y = make_classification(n_samples=100, n_features=2, n_classes=2, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Modelo KNN
knn = KNeighborsClassifier(n_neighbors=3)  # K = 3
knn.fit(X_train, y_train)

# Predição
y_pred = knn.predict(X_test)

# Avaliação
print("Acurácia:", accuracy_score(y_test, y_pred))
```

### Regressão
```python
from sklearn.neighbors import KNeighborsRegressor
import numpy as np

# Dados fictícios
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([2, 4, 5, 8, 10])

# Modelo KNN
knn_reg = KNeighborsRegressor(n_neighbors=2)
knn_reg.fit(X, y)

# Predição
print(knn_reg.predict([[6]]))  # Prever valor para X=6
```