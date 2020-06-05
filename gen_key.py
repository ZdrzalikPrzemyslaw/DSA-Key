import random


def gen_key(p, q, g):
    # Choose an integer x randomly from 1 to q - 1
    x = random.randint(1, q-1)
    # compute y:= g^x mod p
    y = pow(g, x, p)
    # x is the private key and y is the public key.
    return x, y


