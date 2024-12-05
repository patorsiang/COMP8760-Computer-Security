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

# Replay attack simulation
def replay_attack():
    # Known to Eve from the previous session
    K_AB = "0x09f173d29498c59c4613bc51190ccd23b158966468ff6bd7fdcc66d96811e0f2"
    message_3 = "0x81c7ff3...encrypted_message_here..."  # Replace with actual captured encrypted message
    K_BS = "0x16ebe3aelacea4...Bob_server_shared_key..."  # Replace with actual K_BS

    print("\nUnknown to Eve:")
    print(f"[Eve]: Pre-recorded K_AB: {K_AB}")
    print(f"[Eve]: Pre-recorded Message 3: {message_3}")

    # Step 3: Eve sends Message 3 to Bob
    print(f"\n3 (Eve => Bob): Replaying E_{{K_BS}}(K_AB, A) = {message_3}")
    decrypted_message_for_bob = decrypt(K_BS, message_3)
    print(f"[Bob]: Decrypted message: {decrypted_message_for_bob}")

    # Step 4: Bob generates a nonce (N_B)
    N_B = generate_nonce()
    print(f"\n4 (Bob): N_B = {N_B}")
    encrypted_N_B = encrypt(K_AB, N_B)
    print(f"4 (Bob => Eve): E_{{K_AB}}(N_B) = {encrypted_N_B}")

    # Step 5: Eve intercepts N_B, computes N_B-1, and sends it back to Bob
    decrypted_N_B = decrypt(K_AB, encrypted_N_B)
    print(f"[Eve]: Decrypted N_B = {decrypted_N_B}")
    N_B_minus_1 = str(int(decrypted_N_B) - 1)
    encrypted_N_B_minus_1 = encrypt(K_AB, N_B_minus_1)
    print(f"\n5 (Eve => Bob): E_{{K_AB}}(N_B-1) = {encrypted_N_B_minus_1}")

    # Bob decrypts and verifies
    decrypted_N_B_minus_1 = decrypt(K_AB, encrypted_N_B_minus_1)
    print(f"[Bob]: Decrypted N_B-1 = {decrypted_N_B_minus_1}")
    if decrypted_N_B_minus_1 == str(int(N_B) - 1):
        print("=> Eve successfully impersonated Alice!")
    else:
        print("=> Attack failed!")

# Run the replay attack
if __name__ == "__main__":
    replay_attack()
