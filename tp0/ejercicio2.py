# Ejercicio 2:
#   Programar una función que tome como entrada el diccionario del ejercicio 1 y devuelva
#   una "LISTA" con símbolos ordenados en forma descendente según la cantidad de ocurrencias. Luego
#   imprimir en forma de tabla en la columna 1 el símbolo y en la columna 2 la cantidad de
#   ocurrencias.

def sort_by_occurrences(dictionary: dict):
    if not isinstance(dictionary, dict):
        print(f"ERROR! Se esperaba un parametro tipo dict")
        return []

    # El parámetro "key" indica a la func, respecto a que ordenar.
    list_of_key_sorted = list(dict(sorted(dictionary.items(), key=lambda item: item[1], reverse=True)).keys())
    return  list_of_key_sorted