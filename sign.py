import random
# Choose an approved cryptographic hash function H with output length |H| bits. In the original DSS, H was always SHA-1
from hashlib import sha1


def rozszerzony_alogrytm_euklidesa(a, b):  #a, b względnie pierwsze
    # algorytm zwraca odwrotne modulo a względem b używając rozszerzonego algorytmu euklidesa
    # źródło https://www.geeksforgeeks.org/multiplicative-inverse-under-modulo-m/
    b0 = b
    y = 0
    x = 1

    if b == 1:
        return 0

    while a > 1:
        q = a // b
        t = b
        b = a % b
        a = t
        t = y

        y = x - q * y
        x = t

    if x < 0:
        x = x + b0

    return x


# A message m is signed as follows:
def sign(p, q, g, x, m):
    # choose an integer k randomly from 1 to q - 1
    k = random.randint(1, q-1)
    # compute r:= (g ^ k % p) % q
    r = pow(g, k , p) % q
    # compute s:= (k^-1 * (SHA-1(m) + x * r)) %q
    k_odw = rozszerzony_alogrytm_euklidesa(k,q)
    s = (k_odw * (int(sha1(m.encode('utf-8')).hexdigest(), 16) + x * r)) % q
    # if r = 0 start again with a different k
    # In the unlikely case that s=0, start again with a different random k.
    while r == 0 or s == 0:
        k = random.randint(1, q - 1)
        r = pow(g, k, p) % q
        k_odw = rozszerzony_alogrytm_euklidesa(k, q)
        s = (k_odw * (int(sha1(m.encode('utf-8')).hexdigest(), 16) + x * r)) % q
    # the signature is (r,s)
    return r, s


# One can verify that a signature (r, s) is a valid signature for a message m as follows:
def verify_signature(p, q, g, r, s, m, y):
    # Verify that  0 < r < q and 0 < s < q
    if r <= 0 or r >= q:
        return False
    elif s <= 0 or s >= q:
        return False
    # compute w:= s^-1 % q
    w = rozszerzony_alogrytm_euklidesa(s, q)
    # compute u_1 = SHA-1(m) * w mod q
    u_1 = (int(sha1(m.encode('utf-8')).hexdigest(), 16) * w) % q
    # compute u_2 = r * w mod q
    u_2 = r * w % q
    # compute v:=(g^u_1 * y^u_2 %p)%q
    v_1 = pow(g, u_1, p)
    v_2 = pow(y, u_2, p)
    v = ((v_1 * v_2)% p ) % q
    # the signature i valid if and only if v = r
    if v == r:
        return True
    else:
        return False


print(rozszerzony_alogrytm_euklidesa(4,19))