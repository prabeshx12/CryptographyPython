import hashlib


def sha256_hash(plain_text):
    # Creating a sha256 hash object
    sha256_hash_ = hashlib.sha256()

    # Update the hash object with the bytes of the input string
    sha256_hash_.update(plain_text.encode('utf-8'))

    # Return the hexadecimal representation of the hash
    return sha256_hash_.hexdigest()


input_string = "hello world"
hashed_string = sha256_hash(input_string)
print(f"SHA-256 Hash of '{input_string}': {hashed_string}")
