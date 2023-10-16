class Parser(object):
    """
    Gramática LL1:
        S -> F
        S -> (S+F)
        S -> a
    """

    def __init__(self):
        self.cadena = None

    def evaluate(self, cadena):
        self.cadena = cadena
        self.S()
        return self.cadena[0] == "$"

    def S(self):
        print("S", self.cadena)
        if self.cadena[0] == "a":
            self.F()
            self.S()
        elif self.cadena[0] == "(":
            self.match("(")
            self.S()
        elif self.cadena[0] == "+":
            self.match("+")
            self.S()
        elif self.cadena[0] == ")":
            self.match(")")
            self.S()
        elif self.cadena[0] == "$":
            print("OK")
        else:
            raise Exception("Error", "En S")

    def F(self):
        print("F", self.cadena)
        if self.cadena[0] == "a":
            self.match("a")
        else:
            raise Exception("Error", "En F")

    def match(self, s):
        print("M", self.cadena, s)
        if s == self.cadena[0]:
            self.cadena = self.cadena[1:]
        else:
            raise Exception("Error", "En Match")


if __name__ == "__main__":
    p = Parser()
    word = "((a+a)+a)$"
    print(f"S('{word}') -> {p.evaluate(word)}")
