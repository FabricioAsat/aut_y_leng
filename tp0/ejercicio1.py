# Ejercicio 1:
#   Programar una función que dada una cadena retorne en un diccionario la cantidad de
#   ocurrencias de los símbolos del lenguaje hexadecimal. Σ={ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F}
def contar_concurrencia(string: str = ""):
    hex_matches = '0123456789ABCDEF'
    all_matches = {value: 0 for value in hex_matches}

    for digit in string.upper():
        if digit in all_matches:
            all_matches[digit] += 1

    # Para que quede más bonito en el print()
    final_message = ""
    for digit in all_matches:
        final_message = final_message + digit + ": " + str(all_matches[digit]) + " times\n"

    return all_matches


