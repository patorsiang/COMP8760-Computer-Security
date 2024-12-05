import hashlib

target = "3ddcd95d2bff8e97d3ad817f718ae207b98c7f2c84c5519f89cd15d7f8ee1c3b"

def read_dict_txt():
  with open('phpbb.txt', 'r') as f:
    return [line.strip() for line in f]

def hash_password(password):
  password = password.encode()
  hashed_password = hashlib.sha256(password).hexdigest()
  return hashed_password

dictionary = read_dict_txt()
for word in dictionary:
  h = hash_password(word)
  if h == target:
    print(f"Found password: {word}")
    break
  else:
    print(f"{word}: {h}")
