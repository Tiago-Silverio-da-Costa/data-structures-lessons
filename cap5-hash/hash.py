# Funções hash
def hash_a(string):
    # a. Retorna "1" para qualquer entrada
    return 1

def hash_b(string):
    # b. Usa o comprimento da string como índice
    return len(string) % 10

def hash_c(string):
    # c. Usa o primeiro caractere da string como índice (a=0, b=1, ..., z=25)
    return ord(string[0].lower()) % 10

def hash_d(string):
    # d. Mapeia cada letra para um número primo e retorna a soma % tamanho da tabela
    prime_map = {
        'a': 2, 'b': 3, 'c': 5, 'd': 7, 'e': 11, 'f': 13, 'g': 17, 'h': 19,
        'i': 23, 'j': 29, 'k': 31, 'l': 37, 'm': 41, 'n': 43, 'o': 47, 'p': 53,
        'q': 59, 'r': 61, 's': 67, 't': 71, 'u': 73, 'v': 79, 'w': 83, 'x': 89,
        'y': 97, 'z': 101
    }
    hash_sum = sum(prime_map[char.lower()] for char in string if char.lower() in prime_map)
    return hash_sum % 10

# Dados de teste
phone_book_names = ["Esther", "Ben", "Bob", "Dan"]
battery_sizes = ["A", "AA", "AAA", "AAAA"]
book_titles = ["Maus", "Fun Home", "Watchman"]

# Função para exibir os resultados
def test_hash_functions(data, hash_functions):
    results = {}
    for func_name, func in hash_functions.items():
        results[func_name] = [func(item) for item in data]
    return results

# Dicionário de funções hash
hash_functions = {
    "hash_a": hash_a,
    "hash_b": hash_b,
    "hash_c": hash_c,
    "hash_d": hash_d
}

# Testando as funções hash
print("Phone Book Hashing:")
print(test_hash_functions(phone_book_names, hash_functions))

print("\nBattery Sizes Hashing:")
print(test_hash_functions(battery_sizes, hash_functions))

print("\nBook Titles Hashing:")
print(test_hash_functions(book_titles, hash_functions))
