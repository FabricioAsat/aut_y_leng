from tp1.ejercicio6 import *
from tp1.ejercicio7 import convert


def run_tp1():
    cadenas_a_b = ["0000", "", "-123002", "2", "0", "aaaa", "25", "-345", "101"]
    cadenas_c = ["", "mi_var", "_var_", "mi-var", "_1var", "1var", "var33", "_mivar", "123"]
    cadenas_d = ["", "abc", "aaaaabcccccc", "aabbcc", "aaaaaab", "aaaaa", "bcccc", "aabccccccccc", "abccccccccccc"]
    cadenas_e = ["", "10.0.1.2", "192.168.1.1", "127.0.0.1", "0.0.0.0", "1234.1234.1323.1235", "1.1.1.1.", ".1.1.1.1",
                 "123.123.123.1234"]
    cadenas_f = ["", "10.0.1.2:0000", "192.168.1.1:", "127.0.0.1:60", "0.0.0.0:123", "1234.1234.1323.1235:32",
                 "1.1.1.1:0123"]
    cadenas_g = ["0000 0000 0000 0000", "000 000 000 000", "0000 000 000 000"]

    convert("input.csv", "output.csv")
