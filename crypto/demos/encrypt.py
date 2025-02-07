import random
import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def generate_prime():
    while True:
        prime = random.randint(2 ** 8, 2 ** 16)
        if is_prime(prime):
            return prime

def generate_keypair():
    p = generate_prime()
    q = generate_prime()
    n = p * q
    phi = (p - 1) * (q - 1)

    while True:
        e = random.randint(2, phi)
        if math.gcd(e, phi) == 1:
            break

    d = pow(e, -1, phi)
    return ((n, e), (n, d))

def encrypt(message, public_key):
    n, e = public_key
    encrypted_message = [pow(ord(char), e, n) for char in message]
    return encrypted_message

def bytes_to_long(message):
    return int.from_bytes(message.encode(), 'big')

public_key, private_key = generate_keypair()
print(public_key, private_key)

message = "REDACTED"
encrypted_msg = encrypt(message, public_key)

print("Encrypted message (as long integer):", encrypted_msg)

'''
(1346890901, 1257540563) (1346890901, 630817991)
Encrypted message (as long integer): [429598552, 1270819179, 1140101372, 86576308, 1270819179, 1140101372, 1270819179, 102369940, 1140101372, 276169517, 701637297, 1185312925, 1241220380]
'''

# gcd(e, p - 1) = 1 -> e * x + (p - 1) * y = 1