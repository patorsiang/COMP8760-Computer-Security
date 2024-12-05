import random
import string
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.padding import PKCS7
from cryptography.hazmat.backends import default_backend

# Utility functions for key and nonce generation
def generate_symmetric_key():
    return "0x" + ''.join(random.choices('0123456789abcdef', k=64))  # 64 hex chars

def generate_nonce():
    return ''.join(random.choices(string.digits, k=19))  # 19-digit nonce

# AES encryption function
def encrypt(key, plaintext):
    key_bytes = bytes.fromhex(key[2:])
    plaintext_bytes = plaintext.encode()

    # Pad the plaintext
    padder = PKCS7(128).padder()
    padded_data = padder.update(plaintext_bytes) + padder.finalize()

    # Encrypt using AES in ECB mode
    cipher = Cipher(algorithms.AES(key_bytes), modes.ECB(), backend=default_backend())
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(padded_data) + encryptor.finalize()
    return "0x" + ciphertext.hex()

# AES decryption function
def decrypt(key, ciphertext):
    key_bytes = bytes.fromhex(key[2:])
    ciphertext_bytes = bytes.fromhex(ciphertext[2:])

    # Decrypt using AES in ECB mode
    cipher = Cipher(algorithms.AES(key_bytes), modes.ECB(), backend=default_backend())
    decryptor = cipher.decryptor()
    padded_plaintext = decryptor.update(ciphertext_bytes) + decryptor.finalize()

    # Unpad the plaintext
    unpadder = PKCS7(128).unpadder()
    plaintext_bytes = unpadder.update(padded_plaintext) + unpadder.finalize()
    return plaintext_bytes.decode()

# Main function simulating the Needham-Schroeder protocol
def needham_schroeder_protocol():
    # Step 0: Pre-shared keys
    K_AS = generate_symmetric_key()  # Key between Alice and Server
    K_BS = generate_symmetric_key()  # Key between Bob and Server
    print(f"Pre-shared key between Alice and Server: {K_AS}")
    print(f"Pre-shared key between Bob and Server: {K_BS}")

    # Step 1: Alice generates a nonce and sends it to the server
    N_A = generate_nonce()
    print(f"\n1 (Alice): N_A = {N_A}")
    print(f"1 (Alice => Server): (A, B, N_A) = (Alice, Bob, {N_A})")

    # Step 2: Server generates a session key and sends encrypted messages to Alice
    K_AB = generate_symmetric_key()  # Session key for Alice and Bob
    print(f"\n2 (Server): K_AB = {K_AB}")
    message_for_bob = f"{K_AB}, Alice"
    encrypted_message_for_bob = encrypt(K_BS, message_for_bob)  # Encrypted for Bob
    print(f"2 (Server) E_{{K_BS}}(K_AB, A) = E_{{{K_AB}}}({message_for_bob}) = {encrypted_message_for_bob}")
    message_for_alice = f"{N_A}, Bob, {K_AB}, {encrypted_message_for_bob}"
    encrypted_message_for_alice = encrypt(K_AS, message_for_alice)  # Encrypted for Alice
    print(f"2 (Server => Alice): E_{{K_AS}}(N_A, B, K_AB, E_{{K_BS}}(K_AB, A)) = E_{{{K_AS}}}({message_for_alice}) = {encrypted_message_for_alice}")
    decrypted_message_for_alice = decrypt(K_AS, encrypted_message_for_alice)
    print(f"2 (Alice) (N_A, B, K_AB, E_{{K_BS}}(K_AB, A)) = ({decrypted_message_for_alice})")
    if decrypted_message_for_alice == message_for_alice:
        print("=> Message 2 authentication was successful!")
    else:
        print("=> Message 2 authentication failed!")

    # Step 3: Alice decrypts the server's message and forwards Bob's part to Bob
    print(f"\n3 (Alice => Bob): E_{{K_BS}}(K_AB, A) = E_{{{K_BS}}}({message_for_bob}) = {encrypted_message_for_bob}")
    decrypted_message_for_bob = decrypt(K_BS, encrypted_message_for_bob)
    print(f"3 (Bob): (K_AB, A): ({decrypted_message_for_bob})")
    if decrypted_message_for_bob == message_for_bob:
        print("=> Message 3 authentication was successful!")
    else:
        print("=> Message 3 authentication failed!")

    # Step 4: Bob decrypts Alice's message and generates a nonce
    N_B = generate_nonce()
    print(f"\n4 (Bob): N_B = {N_B}")
    encrypted_N_B = encrypt(K_AB, N_B)
    print(f"4 (Bob => Alice): E_{{K_AB}}(N_B): E_{{{K_AB}}}({N_B}) = {encrypted_N_B}")
    decrypted_N_B = decrypt(K_AB, encrypted_N_B)
    print(f"4 (Alice): N_B = {decrypted_N_B}")
    if decrypted_N_B == N_B:
       print("=> Message 4 authentication was successful!")
    else:
        print("=> Message 4 authentication failed!")

    N_B_minus_1 = str(int(decrypted_N_B) - 1)
    encrypted_N_B_minus_1 = encrypt(K_AB, N_B_minus_1)
    print(f"\n5 (Alice => Bob): E_{{K_AB}}(N_B-1) = {encrypted_N_B_minus_1}")
    decrypted_N_B_minus_1 = decrypt(K_AB, encrypted_N_B_minus_1)
    print(f"5 (Bob): N_B-1 = {decrypted_N_B_minus_1}")
    if decrypted_N_B_minus_1 == str(int(N_B) - 1):
        print("=> Message 5 authentication was successful!")
        print(f"\nThe key agreed between Alice and Bob: {K_AB}")
    else:
        print("=> Message 5 authentication failed!")

# Run the protocol simulation
if __name__ == "__main__":
    needham_schroeder_protocol()
