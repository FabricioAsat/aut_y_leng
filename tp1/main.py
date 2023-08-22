from ejercicio6 import *

if __name__ == '__main__':

    cadenas_a_b = ["0000", "", "-123002", "2", "0", "aaaa", "25", "-345", "101"]
    cadenas_c = ["", "mi_var", "_var_", "mi-var", "_1var", "1var", "var33", "_mivar", "123"]
    cadenas_d = ["", "abc", "aaaaabcccccc", "aabbcc", "aaaaaab", "aaaaa", "bcccc", "aabccccccccc", "abccccccccccc"]
    cadenas_e = ["", "10.0.1.2", "192.168.1.1", "127.0.0.1", "0.0.0.0", "1234.1234.1323.1235", "1.1.1.1.", ".1.1.1.1",
                 "123.123.123.1234"]
    cadenas_f = ["", "10.0.1.2:0000", "192.168.1.1:", "127.0.0.1:60", "0.0.0.0:123", "1234.1234.1323.1235:32",
                 "1.1.1.1:0123"]
    cadenas_g = ["0000 0000 0000 0000", "000 000 000 000", "0000 000 000 000"]

    print("\n\nEjercicio a:")
    for string in cadenas_a_b:
        if validate_a(string):
            print(string, "es un número par")
        else:
            print(string, "NO es un número par")

    print("\n\nEjercicio b:")

    for string in cadenas_a_b:
        if validate_b(string):
            print(string, "es un número par válido")
        else:
            print(string, "NO es un número par válido o tiene ceros innecesarios")

    print("\n\nEjercicio c:")
    for string in cadenas_c:
        if validate_c(string):
            print(string, "es una variable de python posible")
        else:
            print(string, "NO puede ser una variable de python")

    print("\n\nEjercicio d:")
    for string in cadenas_d:
        if validate_d(string):
            print(string, "responde a: a^n b c^m")
        else:
            print(string, "NO responde a: a^n b c^m")

    print("\n\nEjercicio e:")
    for string in cadenas_e:
        if validate_e(string):
            print(string, "es una dirección ipv4 posible")
        else:
            print(string, "NO es una dirección ipv4")

    print("\n\nEjercicio f:")

    for string in cadenas_f:
        if validate_f(string):
            print(string, "es una dirección ipv4 con puerto posible")
        else:
            print(string, "NO es una dirección con puerto ipv4")

    print("\n\nEjercicio g:")

    for string in cadenas_g:
        if validate_g(string):
            print(string, "es un núm válido VISA")
        else:
            print(string, "NO es un núm válido VISA")
