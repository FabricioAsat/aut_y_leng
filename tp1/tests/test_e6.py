from tp1.ejercicio6 import (
    validate_a,
    validate_b,
    validate_c,
    validate_d,
    validate_e,
    validate_f,
    validate_g,
)


def test_e6_a():
    v = [
        ("20", True),
        ("-344", True),
        ("-02", True),
        ("2", True),
        ("0", True),
        ("00344", True),
        ("1", False),
        ("-1", False),
        ("-000001", False),
    ]
    for t in v:
        if validate_a(t[0]) == t[1]:
            print(f"'{t[0]}' - OK")
        else:
            print(f"{t[0]}' - ERROR")


def test_e6_b():
    v = [
        ("20", True),
        ("-344", True),
        ("-02", False),
        ("2", True),
        ("0", True),
        ("00344", False),
        ("1", False),
        ("-1", False),
        ("-000001", False),
    ]
    for t in v:
        if validate_b(t[0]) == t[1]:
            print(f"'{t[0]}' - OK")
        else:
            print(f"{t[0]}' - ERROR")


def test_e6_c():
    v = [
        ("foo", True),
        ("_foo", True),
        ("_0foo_______FOO", True),
        ("_____Foo_______FOO", True),
        ("0foo", False),
        ("-0foo", False),
        ("foo-bar-baz", False),
    ]
    for t in v:
        if validate_c(t[0]) == t[1]:
            print(f"'{t[0]}' - OK")
        else:
            print(f"{t[0]}' - ERROR")


def test_e6_d():
    v = [
        ("aaaabccccc", True),
        ("abbbbc", False),
        ("caaab", False),
        ("abc", True),
        ("abccccccccccc", True),
        ("aaaaaaaaaaaaabc", True),
        ("ac", False),
        ("", False),
    ]
    for t in v:
        if validate_d(t[0]) == t[1]:
            print(f"'{t[0]}' - OK")
        else:
            print(f"{t[0]}' - ERROR")


def test_e6_e():
    v = [
        ("", False),
        ("127.0.0.1", True),
        ("0.0.0.0", True),
        ("255.255.255.255", True),
        ("10.20.30.40", True),
        ("10.256.30.40", False),
        ("10.20.030.40", False),
        ("127.0.1", False),
        ("127.0.0.0.1", False),
        ("..255.255", False),
        (" 127.0.0.1", False),
        ("127.0.0.1 ", False),
        (" 127.0.0.1 ", False),
    ]
    for t in v:
        if validate_e(t[0]) == t[1]:
            print(f"'{t[0]}' - OK")
        else:
            print(f"'{t[0]}' - ERROR")


def test_e6_f():
    v = [
        ("", False),
        ("127.0.0.1:", False),
        ("127.0.0.1:80", True),
        ("127.0.0.1:65535", True),
        ("0.0.0.0", True),
        ("0.0.0.0:65536", False),
        ("255.255.255.255", True),
        ("10.20.30.40", True),
        ("10.256.30.40", False),
        ("10.20.030.40", False),
        ("127.0.1", False),
        ("127.0.1:8080", False),
        ("127.0.0.0.1", False),
        ("..255.255", False),
        (" 127.0.0.1", False),
        ("127.0.0.1 ", False),
        (" 127.0.0.1 ", False),
    ]
    for t in v:
        if validate_f(t[0]) == t[1]:
            print(f"'{t[0]}' - OK")
        else:
            print(f"{t[0]}' - ERROR")


def test_e6_g():
    v = [
        ("412458596800791", False),
        ("4124585968007917", True),
        ("4074442565742969", True),
        ("4080649537159229", True),
        ("3080649537159229", False),
        ("4404918027486", True),
        ("1111335754105", False),
    ]
    for t in v:
        if validate_g(t[0]) == t[1]:
            print(f"'{t[0]}' - OK")
        else:
            print(f"{t[0]}' - ERROR")


def run_tests_tp1_ej6():
    print("\nTest E6 a):")
    test_e6_a()
    print("\nTest E6 b):")
    test_e6_b()
    print("\nTest E6 c):")
    test_e6_c()
    print("\nTest E6 d):")
    test_e6_d()
    print("\nTest E6 e):")
    test_e6_e()
    print("\nTest E6 f):")
    test_e6_f()
    print("\nTest E6 g):")
    test_e6_g()
