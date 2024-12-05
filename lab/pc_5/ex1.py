import hashlib
import random

model = dict()

def hash_password_with_salt (password, salt = random.randint(0, 100)):
  salt = str(salt)
  password += str(salt)
  password = password.encode()
  hashed_password = hashlib.sha256(password).hexdigest()
  return hashed_password, salt

def register (username, password):
  password_hash, salt = hash_password_with_salt(password)
  model[username] = {'password': password_hash, 'salt': salt}
  print(f"{username} is registered completely")

def login (username, password):
  if username in model:
    password_hash, _ = hash_password_with_salt(password, model[username]['salt'])
    if password_hash == model[username]['password']:
      print(f"{username} is logged in successfully")
    else:
      print("Invalid password")
  else:
    print("User not found")

# testing functions
register("user1", "password1")
register("user2", "password1")

login("user1", "password1")  # Should work
login("user2", "password1")  # Should work
login("user1", "wrong_password")  # Invalid password
login("user3", "password2")  # User not found

# Observing vulnerabilities
print(f"Hashes stored in model: {model}")
if model["user1"]["password"] == model["user2"]["password"]:
    print("User 1 and User 2 passwords are same.")
