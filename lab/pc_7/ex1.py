import hmac
import hashlib
import random
import binascii

# Function to generate a 16-bit HMAC
def generate_hmac(key, message):
    full_hmac = hmac.new(key.encode(), message.encode(), hashlib.sha256).digest()
    truncated_hmac = binascii.hexlify(full_hmac)[:4]  # Take only the first 4 hex characters (16 bits)
    return truncated_hmac

# Example transaction
key = "secret_key"
message = "Alice, Bob, £10"
hmac_value = generate_hmac(key, message)

print(f"Message: {message}")
print(f"HMAC: {hmac_value.decode()}")

# Eve's attack: change the message without updating the HMAC
eve_message = "Alice, Eve, £1000"
eve_hmac = hmac_value  # Eve doesn't know the key and keeps the same HMAC

# Bank server verification
def verify_hmac(key, message, received_hmac):
    calculated_hmac = generate_hmac(key, message)
    return calculated_hmac == received_hmac

print(f"Eve's attack:")
print(f"Manipulated Message: {eve_message}")
print(f"Server verification: {'Accepted' if verify_hmac(key, eve_message, eve_hmac) else 'Rejected'}")

# Brute force simulation by Eve
attempts = 0
while True:
    attempts += 1
    test_hmac = binascii.hexlify(random.randbytes(2))  # Random 16-bit value
    if test_hmac == hmac_value:
        break

print(f"Attempts needed to guess the correct HMAC: {attempts}")
