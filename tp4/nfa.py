import sys
from code import validate


# * RECORDAR: Solo se deba ejecutar por linea de comando.
class NFA:
    def __init__(self, file=None):
        super(NFA, self).__init__()
        self.path = file

    def run(self, word: str):
        return validate(self.path, word)


try:
    path = sys.argv[1]  # Primer argumento (file.jff)
    word = sys.argv[2]  # Segundo argumento (110)
    nfa = NFA(path)
    print(nfa.run(word))
except:
    print("Introduce las variables por consola")
