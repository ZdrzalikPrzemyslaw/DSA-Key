from file_io_krypto import write_to_file_parameters, read_file_parameters, write_to_file_public_key, \
    write_to_file_private_key, read_file_private_key, read_file_public_key, read_file_message, \
    write_to_file_sign, read_file_sign
from gen_param import gen_param
from gen_key import gen_key
from sign import sign, verify_signature







def choose_mode():
    i = -1
    while i not in [1, 2, 3, 4, 5]:
        print("1. Wygeneruj Parametry \n"
              "2. Wygeneruj klucz prywatny i publiczny \n"
              "3. Utwórz podpis cyfrowy \n"
              "4. Zweryfikuj  podpis cyfrowy \n"
              "5. Wylacz program")
        try:
            i = int(input())
        except ValueError:
            print("zly input")
            pass
    return i


def wybor_1():
    L = -1
    while L > 1024 or L < 512 or L % 64 != 0:
        try:
            L = int(input("Podaj dlugosc klucza w bitach, dlugosc musi znajdowac sie "
                          "w przedziale od 512 do 1024 ( 512, 576, 640, 704, 768, 832, 896, 960, 1024)"
                          " i byc podzielna przez 64 \n"))
        except ValueError:
            print("zly input")
            pass
    p, q, g = gen_param(L)
    write_to_file_parameters(p, q, g)


def wybor_2():
    p, q, g = read_file_parameters()
    if p == -1:
        fail = "a"
        while fail != "n" and fail != "T":
            fail = input("nie udalo sie otworzyc pliku z parametrami funkcji, czy chcesz teraz wygenerowac? [T,n] \n")
            if fail != "n" and fail != "T":
                print("prosze podać T lub n ")
        if fail == "n":
            return
        elif fail == "T":
            wybor_1()
            p, q, g = read_file_parameters()
            if p == -1:
                print("nie udalo sie wygenerowac parametrow")
                return
    x, y = gen_key(p, q, g)
    write_to_file_public_key(y)
    write_to_file_private_key(x)


def wybor_3():
    p, q, g = read_file_parameters()
    if p == -1:
        fail = "a"
        while fail != "n" and fail != "T":
            fail = input("nie udalo sie otworzyc pliku z parametrami funkcji, czy chcesz teraz wygenerowac? [T,n] \n")
            if fail != "n" and fail != "T":
                print("prosze podać T lub n")
        if fail == "n":
            return
        elif fail == "T":
            wybor_1()
            p, q, g = read_file_parameters()
            if p == -1:
                print("nie udalo sie wygenerowac parametrow")
                return
    x = read_file_private_key()
    if x == -1:
        return
    choice = "a"
    while choice != "P" and choice != "k":
        choice = input("czy chcesz wygenerowac podpis z pliku czy z konsoli? [P,k] \n")
        if choice != "P" and choice != "k":
            print("prosze podać P lub k")
    message = ""
    if choice == "k":
        while message == "":
            message = input("podaj wybrana wiadomosc \n")
            if message == "":
                print("nie udalo sie odczytac wiadomosci lub wiadomosc "
                      "jest pusta, prosze wprowadzic wiadomosc przez konsole")
    elif choice == "P":
        message = ""
        file = input("podaj nazwe pliku \n")
        message = read_file_message(file)
        while message == -1:
            print("nie udalo sie odczytac wiadomosci lub wiadomosc "
                  "jest pusta, prosze wprowadzic wiadomosc przez konsole")
            message = input("podaj wybrana wiadomosc \n")
    r, s = sign(p, q, g, x, message)
    write_to_file_sign(r, s)


def wybor_4():
    p, q, g = read_file_parameters()
    if p == -1:
        return
    y = read_file_public_key()
    if y == -1:
        return
    choice = "a"
    while choice != "P" and choice != "k":
        choice = input("czy chcesz sprawdzic podpis wiadomosci z pliku czy z konsoli? [P,k] \n")
        if choice != "P" and choice != "k":
            print("prosze podać P lub k")
    message = ""
    if choice == "k":
        while message == "":
            message = input("podaj wybrana wiadomosc \n")
            if message == "":
                print("nie udalo sie odczytac wiadomosci lub wiadomosc "
                      "jest pusta, prosze wprowadzic wiadomosc przez konsole")
    elif choice == "P":
        file = input("podaj nazwe pliku \n")
        message = read_file_message(file)
        while message == -1:
            print("nie udalo sie odczytac wiadomosci lub wiadomosc "
                  "jest pusta, prosze wprowadzic wiadomosc przez konsole")
            message = input("podaj wybrana wiadomosc \n")
    r, s = read_file_sign()
    is_good_signature = verify_signature(p, q, g, r, s, message, y)
    if is_good_signature:
        print("podpis wiadomosci jest poprawny")
        return
    print("podpis wiadomosci jest nie poprawny")
