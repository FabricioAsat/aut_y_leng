# Utilizar el módulo re(expresiones regulares) de Python para validar cadenas
# pertenecientes a los siguientes lenguajes

import re
from typing import Match


# Números enteros pares (ej. 20, -344, -02, 2, 0, 00344)
def validate_a(value: str) -> bool:
    if len(value) == 0:
        print("No se acepta cadenas vacías.")
        return False
    pair_numbers = r'^-?\d*[02468]$'
    return bool(re.match(pair_numbers, value))


# Números enteros pares sin ceros no significativos (no puede generar -02)
def validate_b(value: str) -> bool:
    if len(value) == 0:
        print("No se acepta cadenas vacías.")
        return False
    pair_numbers_fixed = r'^-?([1-9]*[02468]$)'
    return bool(re.match(pair_numbers_fixed, value))


# Nombre de variables en Python, un identificador comienza con una letra minúscula o un
# guión bajo (_) seguido de cero o más letras minúsculas, guión bajo o dígitos (0 a 9).
def validate_c(value: str) -> bool:
    if len(value) == 0:
        print("No se acepta cadenas vacías.")
        return False
    python_vars = r'^[_|(a-z)]+\w*[^-. ]$'
    return bool(re.match(python_vars, value))


# {a^n b c^m / n,m ∈| N* ^ n>0 ^ m>0 } , con Σ = {a, b, c}
def validate_d(value: str) -> bool:
    if len(value) == 0:
        print("No se acepta cadenas vacías.")
        return False
    python_vars = r'^a+b{1}c+$'
    return bool(re.match(python_vars, value))


# Direcciones IPv4 (ej. 10.0.1.2, 192.168.1.1, 127.0.0.1, etc.).
def validate_e(value: str) -> bool:
    if len(value) == 0:
        print("No se acepta cadenas vacías.")
        return False
    string_ipv4 = r'^\d{1,3}(.\d{1,3}){3}$'
    return bool(re.match(string_ipv4, value))


# Direcciones IPv4 con puerto (ej. 127.0.0.1:8080, 127.0.0.1:4200, 127.0.0.1:80)
def validate_f(value: str) -> bool:
    if len(value) == 0:
        print("No se acepta cadenas vacías.")
        return False
    string_ipv4 = r'^\d{1,3}(.\d{1,3}){3}:\d+$'
    return bool(re.match(string_ipv4, value))


def validate_g(value: str) -> bool:
    if len(value) == 0:
        print("No se acepta cadenas vacías.")
        return False
    regex_visa_card = r'^\d{4}((( \d{4}){3}$)|( \d{3}){3}$)'
    return bool(re.match(regex_visa_card, value))
