def triple_rc4_encrypt(key1, key2, key3, data):
    """
    Triple RC4 Encryption
    
    Parâmetros:
    - key1: Primeira chave de criptografia (string)
    - key2: Segunda chave de criptografia (string)
    - key3: Terceira chave de criptografia (string)
    - data: Dados a serem criptografados (string)
    
    Retorna:
    - Dados criptografados com Triple RC4 (bytes)
    """
    # Criptografa com a primeira chave
    first_pass = RC4(key1, data)
    # Descriptografa com a segunda chave
    second_pass = RC4(key2, first_pass.decode('latin1'))
    # Criptografa novamente com a terceira chave
    final_pass = RC4(key3, second_pass.decode('latin1'))
    return final_pass

def triple_rc4_decrypt(key1, key2, key3, data):
    """
    Triple RC4 Decryption
    
    Parâmetros:
    - key1: Primeira chave de decriptografia (string)
    - key2: Segunda chave de decriptografia (string)
    - key3: Terceira chave de decriptografia (string)
    - data: Dados a serem decriptados (bytes)
    
    Retorna:
    - Dados decriptados com Triple RC4 (bytes)
    """
    # Descriptografa com a terceira chave
    first_pass = RC4(key3, data.decode('latin1'))
    # Criptografa com a segunda chave
    second_pass = RC4(key2, first_pass.decode('latin1'))
    # Descriptografa novamente com a primeira chave
    final_pass = RC4(key1, second_pass.decode('latin1'))
    return final_pass

# Exemplo de uso do Triple RC4
key1 = "key1secret"
key2 = "key2secret"
key3 = "key3secret"
plaintext = "Hello, World!"

# Criptografa o plaintext com Triple RC4
encrypted_triple_rc4 = triple_rc4_encrypt(key1, key2, key3, plaintext)
print(f"Encrypted with Triple RC4: {encrypted_triple_rc4}")

# Descriptografa o ciphertext com Triple RC4
decrypted_triple_rc4 = triple_rc4_decrypt(key1, key2, key3, encrypted_triple_rc4)
print(f"Decrypted with Triple RC4: {decrypted_triple_rc4.decode('latin1')}")
