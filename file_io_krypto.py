def write_to_file_parameters(p,q,g):
    try:
        p_plik = open("DSA_p.txt", "w+")
        q_plik = open("DSA_q.txt", "w+")
        g_plik = open("DSA_g.txt", "w+")
    except IOError:
        print("Nie udalo sie otworzyc pliku parametrow")
        return -1
    p_plik.write(str(p))
    q_plik.write(str(q))
    g_plik.write(str(g))
    p_plik.close()
    q_plik.close()
    g_plik.close()
    print("zapisano parametry funkcji w plikach DSA_p.txt DSA_q.txt DSA_g.txt")


def write_to_file_public_key(y):
    try:
        public_key_plik = open("DSA_public_key.txt", "w+")
    except IOError:
        print("Nie udalo sie otworzyc pliku klucza publicznego")
        return -1
    public_key_plik.write((str(y)))
    public_key_plik.close()
    print("zapisano klucz publiczny w pliku DSA_public_key.txt")


def write_to_file_private_key(x):
    try:
        private_key_plik = open("DSA_private_key.txt", "w+")
    except IOError:
        print("Nie udalo sie otworzyc pliku klucza prywatnego")
        return -1
    private_key_plik.write((str(x)))
    private_key_plik.close()
    print("zapisano klucz prywatny w pliku DSA_private_key.txt")


def write_to_file_sign(r, s):
    try:
        r_plik = open("DSA_r.txt", "w+")
        s_plik = open("DSA_s.txt", "w+")
    except IOError:
        print("Nie udalo sie otworzyc pliku podpisu")
        return -1
    r_plik.write(str(r))
    s_plik.write(str(s))
    r_plik.close()
    s_plik.close()
    print("zapisano podpis w plikach DSA_r.txt i DSA_s.txt ")


def read_file_parameters():
    try:
        p_plik = open("DSA_p.txt", "r+")
        q_plik = open("DSA_q.txt", "r+")
        g_plik = open("DSA_g.txt", "r+")
    except IOError:
        print("Nie udalo sie otworzyc pliku parametrow")
        return -1, -1, -1
    p = int(p_plik.read())
    q = int(q_plik.read())
    g = int(g_plik.read())
    p_plik.close()
    q_plik.close()
    g_plik.close()
    return p, q, g


def read_file_public_key():
    try:
        public_key_plik = open("DSA_public_key.txt", "r+")
    except IOError:
        print("Nie udalo sie otworzyc pliku klucza publicznego")
        return -1
    y = int(public_key_plik.read())
    public_key_plik.close()
    return y


def read_file_private_key():
    try:
        private_key_plik = open("DSA_private_key.txt", "r+")
    except IOError:
        print("Nie udalo sie otworzyc pliku klucza prywatnego")
        return -1
    x = int(private_key_plik.read())
    private_key_plik.close()
    return x


def read_file_sign():
    try:
        r_plik = open("DSA_r.txt", "r+")
        s_plik = open("DSA_s.txt", "r+")
    except IOError:
        print("Nie udalo sie otworzyc pliku podpisu")
        return -1, -1
    r = int(r_plik.read())
    s = int(s_plik.read())
    r_plik.close()
    s_plik.close()
    return r, s


def read_file_message(message):
    try:
        message_plik = open(message, "r+")
    except IOError:
        print("Nie udalo sie otworzyc pliku wiadomosci")
        return -1
    message = message_plik.read()
    message_plik.close()
    return message
