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
            self.match("a")
            self.T()
        else:
            pass

    def T(self):
        print("T", self.cadena)
        if self.cadena[0] == "a":
            self.match("a")
            self.S()
            self.match("b")
            self.match("b")
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
    word = "aabb$"
    print(f"S('{word}') -> {p.evaluate(word)}")
