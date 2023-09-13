import json


def validate(string: str):
    with open("tp2/file.json") as json_f:
        automaton = json.load(json_f)

        todos_los_q = automaton["Q"]
        todos_los_sigma = automaton["Sigma"]
        todos_los_gamma = automaton["Gamma"]
        todos_los_delta = automaton["Delta"]
        todos_los_b = automaton["B"]
        todos_los_q0 = automaton["q0"]
        todos_los_f = automaton["F"]

        print("Q: ", todos_los_q)
        print("Sigma: ", todos_los_sigma)
        print("Gamma: ", todos_los_gamma)
        print("Delta: ", todos_los_delta)
        print("B: ", todos_los_b)
        print("Q0: ", todos_los_q0)
        print("F: ", todos_los_f)

        for letter in string:
            
            
            pass


validate("01010101010101")
