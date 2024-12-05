import hashlib
from datetime import date
from itertools import permutations
from multiprocessing import Pool, cpu_count
import time

# Target hash value and salt
target = "3281e6de7fa3c6fd6d6c8098347aeb06bd35b0f74b96f173c7b2d28135e14d45" # -> Woof122981Eltrofor
# target = "fc2298f491eac4cff95e7568806e088a901c904cda7dd3221f551e5b89b3c3aa" # ->
salt = "5UA@/Mw^%He]SBaU"

# Personal information dictionary
info = {
    "username": "laplusbelle",
    "name": "Marie",
    "surname": "Curie",
    "pet": "Woof",
    "birthdate": date(1980, 1, 2),
    "employer": "UKC",
    "mother_first_name": "Jean",
    "mother_last_name": "Neoskour",
    "father_first_name": "Jvaist",
    "father_last_name": "Fairecourir",
    "husband": "Eltrofor",
    "husband_birthdate": date(1981, 12, 29)
}

# Function to format a date in multiple formats
def format_date(date):
    return list(set([str(int(date.strftime(fmt))) for fmt in [
        "%d", "%m"
    ]] + [date.strftime(fmt) for fmt in [
        "%d", "%m", "%y", "%Y"
    ]] + [date.strftime(fmt) for fmt in [
        "%b", "%B"
    ]]))

# Function to gather all information pieces into a list
def info_list():
    result_list = [info[key] for key in info.keys() if type(info[key]) is str]
    for key in info:
        if type(info[key]) is not str:
            result_list += format_date(info[key])
    return result_list

# Hash the password using SHA256
def hash_password(password):
    password = password.encode()
    hashed_password = hashlib.sha256(password).hexdigest()
    return hashed_password

def format_styles(combo):
    # camel_case = combo[0].lower() + ''.join(word.capitalize() for word in combo[1:])
    pascal_case = ''.join(word.capitalize() for word in combo)
    # snake_case = '_'.join(word.lower() for word in combo)
    # kebab_case = '-'.join(word.lower() for word in combo)
    # all_uppercase = '_'.join(word.upper() for word in combo)

    return set([
    #   camel_case,
      pascal_case,
    #   snake_case,
    #   kebab_case,
    #   all_uppercase
    ])

# Worker function for multiprocessing
def worker(combo):
    # password = ''.join(word.capitalize() for word in combo)  # Example style: PascalCase
    # hashed_password = hash_password(password+salt)
    # return password if hashed_password == target else None
    passwords = format_styles(combo)
    for password in passwords:
        hashed_password = hash_password(password+salt)
        if hashed_password == target:
            return password
    return None

# Function to check the target hash against all generated combinations using multiprocessing
def check_target_multiprocessing():
    infolist = info_list()
    print(f"base word numbers: {len(infolist)}")
    for length in range(1, len(infolist)):  # Limit to lengths 1 to 3 for practicality
        print(f"Trying length: {length}")
        start_time = time.time()

        combinations = list(permutations(infolist, length))  # Convert to list to avoid re-iterating
        data_size = len(combinations)
        core = cpu_count()

        with Pool(processes=min(core, data_size)) as pool:  # Limit pool size to avoid overload
            results = pool.imap_unordered(worker, combinations, chunksize=data_size//core)

            for result in results:
                if result:
                    print(f"Password found: {result}")
                    end_time = time.time()
                    elapsed_time = end_time - start_time
                    print(f"No password found for length {length}. Elapsed Time: {elapsed_time:.2f} seconds")
                    pool.terminate()  # Terminate pool once the password is found
                    return result

        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"No password found for length {length}. Elapsed Time: {elapsed_time:.2f} seconds")

    return None

# Run the target checking function
if __name__ == "__main__":
    print(f"target: {target}")
    found_password = check_target_multiprocessing()
    if found_password:
        print(f"Password found: {found_password}")
    else:
        print("No password matched the target hash.")
