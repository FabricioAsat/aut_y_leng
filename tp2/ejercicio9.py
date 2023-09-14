import json

"""
Response = {
        "original_string": string,
        "modified_string": string,
        "isValidString": boolean,
    }
"""


def validate(string: str):
    automaton = {}

    with open("tp2/file.json") as json_f:
        automaton = json.load(json_f)
        json_f.close()

    all_symbols = automaton["Gamma"]  # ['0', '1']
    start = automaton["q0"]  # q0
    blank = automaton["B"]  # "#"
    final = automaton["F"]  # ["q3", ...]
    operations = automaton["Delta"]  # {} todos los q

    state = {"q": start, "position": 0}
    response = {
        "original_string": string,
        "modified_string": "",
        "isValidString": False,
    }

    # Inserto el "blank" al final de la cadena
    string_list = list(string + blank)

    # Si hay simbolos en la cadena que no están incluidos en el string dado, automáticamente valido a falso.
    for letter in set(string):
        try:
            all_symbols.index(letter)
        except:
            return response

    i = 0

    while True:
        # Determina si el programa llegó a su final "F"
        for final_symbol in final:
            if state["q"] == final_symbol:
                response["isValidString"] = True

        # ------------- Corta cuando ya es final
        if response["isValidString"] == True:
            response["modified_string"] = "".join(string_list)
            break
        # ---------

        # si 0 está en las operaciones[q0, q1, q2, ...]
        if string_list[state["position"]] in operations[state["q"]]:
            next_q = operations[state["q"]][string_list[state["position"]]]["q"]

            if operations[state["q"]][string_list[state["position"]]]["m"] == "r":
                new_position = state["position"] + 1
            else:
                new_position = state["position"] - 1

            string_list[state["position"]] = operations[state["q"]][
                string_list[state["position"]]
            ]["e"]

            state["q"] = next_q
            state["position"] = new_position

        else:
            return response

    return response
