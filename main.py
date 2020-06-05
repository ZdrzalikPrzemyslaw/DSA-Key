from menu import choose_mode, wybor_1, wybor_2, wybor_3, wybor_4
# en.wikipedia.org/wiki/Digital_Signature_Algorithm







if __name__ == "__main__":
    wybor = -1
    while wybor != 5:
        wybor = choose_mode()  #  1. Wygeneruj Parametry  2. Wygeneruj klucz prywatny i publiczny) 3. Utwórz podpis cyfrowy 4. Zweryfikuj  podpis cyfrowy
        if wybor == 1:
            wybor_1()
        elif wybor == 2:
            wybor_2()
        elif wybor == 3:
            wybor_3()
        elif wybor == 4:
            wybor_4()

