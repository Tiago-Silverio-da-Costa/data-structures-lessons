import numpy as np

# Notas dos usuários
notas_yogi = [5,5,5,4,4]
notas_pinky = [5,4,3,5,2]

# Função para normalizar notas
def normalizar(notas):
    media = np.mean(notas)
    desvio_padrao = np.std(notas)
    return [(nota - media) / desvio_padrao for nota in notas]

notas_normalizadas_yogi = normalizar(notas_yogi)
notas_normalizadas_pinky = normalizar(notas_pinky)

print("Notas Normalizadas Yogi:", notas_normalizadas_yogi)
print("Notas Normalizadas Pinky", notas_normalizadas_pinky)