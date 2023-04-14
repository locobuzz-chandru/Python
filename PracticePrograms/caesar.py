import string


# plain_text = "python"
# shift = 1
#
# alpha = string.ascii_lowercase
# print(alpha)
# shifted = alpha[shift:] + alpha[:shift]
# print(shifted)
# table = str.maketrans(alpha, shifted)
# print(table)
#
# encrypted = plain_text.translate(table)
#
# print(encrypted)


def caesar(text, shift, alphas):
    def shift_alpha(alpha):
        return alpha[shift:] + alpha[:shift]

    shifted_alphas = tuple(map(shift_alpha, alphas))
    final_alpha = ''.join(alphas)
    final_shifted_alpha = ''.join(shifted_alphas)
    table = str.maketrans(final_alpha, final_shifted_alpha)
    return text.translate(table)


plain_text = "Python Programming"


# print(caesar(plain_text, 7, [string.ascii_lowercase, string.ascii_uppercase, string.punctuation]))


# Hashing is the process of scrambling raw information to the extent that it cannot reproduce it back to its original
# form
# In encryption, data is transformed into a secure format that is unreadable unless the recipient has a key

# When a user enters a password, the hash value is calculated and then compared with the table. If it matches one of the
# saved hashes, it’s a valid password and the user can be permitted access

# It takes a piece of information and passes it through a function that performs mathematical operations on the
# plaintext. This function is called the hash function, and the output is called the hash value
#  websites store user passwords in a hashed format for two benefits. It helps foster a sense of privacy, and it lessens
#  the load on the central database since all the digests are of similar size

# The SHA-256 hash can be used as a secure 64 char password
# SHA-256 generates almost unique 32-bit hash

# By default, Django uses the PBKDF2 algorithm with a SHA256 hash (Password-Based Key Derivation Function)
# the length is exactly 64 bits short of a multiple of 512. During the addition, the first bit should be one, and the
# rest of it should be filled with zeroes

# Salts are used to keep passwords safe while they are being stored


# BCrypt Algorithm is used to hash and salt passwords in a secure way
def bcrypt_algo():
    import bcrypt
    password = b'PythonProgram'
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password, salt)
    print("Salt->", salt)
    print("Hashed->", hashed)


# bcrypt_algo()


# hashlib module is an interface for easily hashing messages. This contains many methods that will handle hashing any
# raw message into an encrypted format.
# The main purpose of this module is to use a hash function on a string and encrypt it so that it is very difficult to
# decrypt it
def hashlib_algo():
    import hashlib
    password = 'PythonProgram'
    salt = "5gz"
    data_base_password = password + salt
    hashed = hashlib.md5(data_base_password.encode())
    print(hashed.hexdigest())


# hashlib_algo()


# resistant to attacks such as dictionary attacks, brute-force attacks, and pre-computation attacks
def argon_algo():
    import argon2
    password = b'PythonProgram'
    hashed_password = argon2.hash_password(password)
    print(hashed_password)


argon_algo()
