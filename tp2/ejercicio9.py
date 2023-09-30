import json
import os
import xmltodict


def validate(string: str):
    respose = {}
    # path = "tp2/file.json"
    path = "tp2/3.jff"
    ext = os.path.splitext(path)[1]

    with open(path) as json_f:
        if ext == ".jff":
            automaton = xmltodict.parse(json_f.read())
            json_automaton = transform(automaton)
            respose = resolve(string, json_automaton)

        else:
            automaton = json.load(json_f)
            respose = resolve(string, automaton)

        json_f.close()

    return respose


def transform(aut: dict):
    aut_transf = {"F": [], "q0": "", "B": "#", "Delta": {}, "Gamma": []}
    all_info = aut["structure"]["automaton"]
    gamma_aux = []

    for block in all_info["block"]:
        if "final" in block:
            aut_transf["F"].append("q" + block["@id"])
        if "initial" in block:
            aut_transf["q0"] = "q" + block["@id"]
        aut_transf["Delta"].update({"q" + block["@id"]: {}})
    for trans in all_info["transition"]:
        trans["read"] = "#" if trans["read"] is None else trans["read"]
        gamma_aux.append(trans["read"])
        aut_transf["Delta"]["q" + trans["from"]].update(
            {
                trans["read"]: {
                    "q": "q" + trans["to"],
                    "e": "#" if trans["write"] is None else trans["write"],
                    "m": trans["move"].lower(),
                }
            }
        )
    aut_transf["Gamma"] = list(set(gamma_aux))
    return aut_transf


def resolve(string: str, automaton: dict):
    all_symbols = automaton["Gamma"]  # ['0', '1']
    start = automaton["q0"]  # q0
    blank = automaton["B"]  # "#"
    final = automaton["F"]  # ["q3", ...]
    operations = automaton["Delta"]  # {} todos los q

    print(operations)

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
