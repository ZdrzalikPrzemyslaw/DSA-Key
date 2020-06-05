import random


def sprawdz_zlozonosc_miller_rabin(a, d, n, r):
    if pow(a, d, n) == 1:
        return False
    for j in range(r):
        if pow(a, 2**j * d, n) == n-1:
            return False
    return True


def czy_pierwsza_miller_rabin(n, k=64):  # https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test
    if n != int(n):
        return False
    n = int(n)
    if n == 0 or n == 1:
        return False
    if n == 2 or n == 3:
        return True
    r = 0
    d = n - 1
    while d%2 == 0:
        d = d // 2
        r += 1
    assert(2**r * d == n - 1)
    d = int(d)
    r = int(r)
    for i in range (k):
        a = random.randint(2, n - 2)
        if sprawdz_zlozonosc_miller_rabin(a, d, n, r):
            return False
    return True
