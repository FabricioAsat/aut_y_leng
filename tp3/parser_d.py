class Parser(object):
    def __init__(self):
        self.cadena = None

    def evaluate(self, cadena):
        self.cadena = cadena
        self.S()
        return self.cadena[0] == "$"

    def S(self):
        print("S", self.cadena)
        if self.cadena[0] == "a":
            self.A()
        elif self.cadena[0] == "b":
            self.B()
        else:
            raise Exception("Error", "En S")

    def A(self):
        print("A", self.cadena)
        if self.cadena[0] == "a":
            self.match("a")
            self.A()
        elif self.cadena[0] == "b":
            raise Exception("Error", "En A")
        else:
            pass

    def B(self):
        print("A", self.cadena)
        if self.cadena[0] == "b":
            self.match("b")
            self.B()
        elif self.cadena[0] == "a":
            raise Exception("Error", "En A")
        else:
            pass

    def match(self, s):
        print("M", self.cadena, s)
        if s == self.cadena[0]:
            self.cadena = self.cadena[1:]
        else:
            raise Exception("Error", "En Match")


if __name__ == "__main__":
    p = Parser()
    word = "aaaa$"
    print(f"S('{word}') -> {p.evaluate(word)}")
