# Ejercicio 3:
#   Programar una función que dada una lista de símbolos de un alfabeto cualquiera y una
#   palabra, valide que esa palabra solo está formada por símbolos del alfabeto en cuestión

def check_symbols(word: str, symbols: list, ignore_case: bool = False):
    if ignore_case:
        word = word.lower()
        symbols = [symbol.lower() for symbol in symbols]

    symbols = list(set(symbols))
    is_a_word = True

    for digit in word:
        if symbols.count(digit) == 0:
            is_a_word = False
            break

    return is_a_word
