from tp0.ejercicio1 import contar_concurrencia
from tp0.ejercicio2 import sort_by_occurrences
from tp0.ejercicio3 import check_symbols


def ejecutar_ejercicio_1():
    # Ejercicio 1 - Contar las ocurrencias de valores hexadecimales introducidos por string
    dict_problem1 = contar_concurrencia("000044466FFFFFFFFFFF123555656465475423542366745423423432412321")
    print("Ejercicio 1:\n", dict_problem1)
    return dict_problem1


def ejecutar_ejercicio_2(dict_problem1):
    # Ejercicio 2 - Devolver una lista con las "keys" ordenadas desc.
    list_of_keys_sorted = sort_by_occurrences(dict_problem1)

    print("\nEjercicio 2:")
    if len(list_of_keys_sorted) == 0:
        print("No hay keys en el diccionario")
    else:
        for symbol in list_of_keys_sorted:
            print(f"Symbol '{symbol}' repeated '{dict_problem1[symbol]}' times.")


def ejecutar_ejercicio_3():
    # Ejercicio 3 -
    print("\nEjercicio 3:")
    spanish_alp = [" ", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r",
                   "s", "t", "u", "v", "w", "x", "y", "z"]

    # is_a_text = check_symbols("palabra aleatoria", spanish_alp)  # True
    # is_a_text = check_symbols("¿palabra aleatoria?!", spanish_alp)  # False
    # is_a_text = check_symbols("Palabra no Case Sensitive", spanish_alp, ignore_case=False)  # False
    is_a_text = check_symbols("CasE SEnSItiVe", spanish_alp, ignore_case=True)  # True

    if is_a_text:
        print("Es un texto/palabra construida con el alfabeto dado")
    else:
        print("El texto/palabra no pertenece al alfabeto dado")


def run_tp0():
    dict_problem1 = ejecutar_ejercicio_1()
    ejecutar_ejercicio_2(dict_problem1)
    ejecutar_ejercicio_3()

