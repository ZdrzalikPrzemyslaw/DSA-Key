from miller_rabin import czy_pierwsza_miller_rabin
import random


def gen_prime_bits(bits = 160):
    x = 0
    if bits < 1:
        return False
    while not czy_pierwsza_miller_rabin(x, 64):
        x = random.randrange(2 ** (bits - 1), 2 ** bits)
    return x

# Szukamy takiej liczby pierwszej p, że ma ona dzielnik q 160 bitowy,
# 160 bitów - długość outputu SHA-1, q.bit_length() musi być < L i q.bit_length() <= długości outputu funkcji SHA-1
# ta liczba p ma od 512 do 1024 bitów,
# ale liczba bitów jest podzielna przez 64 - wartości 512, 576, 640, 704, 768, 832, 896, 960, 1024


def gen_prime_L_bit(L = 512 + 64):
    # Choose the modulus length N such that  N<L and N <=|H|
    p = 1
    if L > 1024 or L < 512 or L % 64 != 0:
        return False
    while not (czy_pierwsza_miller_rabin(p) and p.bit_length() == L):
        x = random.randrange(2 ** (L - 160 - 1), 2 ** (L - 160))
        # Choose an N-bit prime q
        q = gen_prime_bits(160)
        # Choose an L-bit prime p such that p − 1 is a multiple of q.
        p = x * q + 1
    return p, q


# Choose a key length L. The original DSS constrained L to be a multiple of 64 between 512 and 1024 inclusive.
def gen_param(L=512+64):
    p, q = gen_prime_L_bit(L)
    # Choose an integer h randomly from 2 to p - 2
    h = random.randint(2, p - 2)
    # Compute g:= h^((p-1/q)) % p
    g = pow(h, int((p - 1) // q), p)
    # In the rare case that g=1 try again with a different h
    while g == 1:
        h = random.randint(2, p - 2)
        g = pow(h, int((p - 1) // q), p)
    return p, q, g

