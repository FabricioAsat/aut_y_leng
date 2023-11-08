# Librería
import xmltodict


def initial(path: str):
    with open(path) as json_f:
        automaton = xmltodict.parse(json_f.read())
        respose = transform(automaton)
        return nfa_to_dfa(respose)


def transform(aut: dict):
    transform_automaton = {
        "states": 0,
        "letters": [],
        "t_func": [],
        "start": 0,
        "final": [],
    }
    all_info = aut["structure"]["automaton"]

    for state in all_info["state"]:
        if "initial" in state:
            transform_automaton["start"] = int(state["@id"])

        if "final" in state:
            transform_automaton["final"].append(int(state["@id"]))

    letters = []
    t_func = []
    for transition in all_info["transition"]:
        t_from = transition["from"]
        t_read = transition["read"]
        t_to = transition["to"]

        t_func.append([int(t_from), t_read, int(t_to)])
        if not t_read in letters:
            letters.append(t_read)

    grouped_data = {}
    for t in t_func:
        key = (t[0], t[1])
        if key in grouped_data:
            grouped_data[key][2].append(t[2])
        else:
            grouped_data[key] = [t[0], t[1], [t[2]]]

    transform_automaton["states"] = len(all_info["state"])
    transform_automaton["letters"] = letters
    transform_automaton["t_func"] = list(grouped_data.values())

    return transform_automaton


def nfa_to_dfa(data: dict):
    dfa_states = 2 ** data["states"]

    dfa_letters = data["letters"]
    dfa_start = data["start"]
    dfa_t_func = []
    dfa_final = []
    q = []

    q.append((dfa_start,))

    nfa_transitions = {}
    dfa_transitions = {}

    for transition in data["t_func"]:
        nfa_transitions[(transition[0], transition[1])] = transition[2]

    for in_state in q:
        for symbol in dfa_letters:
            if len(in_state) == 1 and (in_state[0], symbol) in nfa_transitions:
                dfa_transitions[(in_state, symbol)] = nfa_transitions[
                    (in_state[0], symbol)
                ]

                if tuple(dfa_transitions[(in_state, symbol)]) not in q:
                    q.append(tuple(dfa_transitions[(in_state, symbol)]))
            else:
                dest = []
                f_dest = []

                for n_state in in_state:
                    if (n_state, symbol) in nfa_transitions and nfa_transitions[
                        (n_state, symbol)
                    ] not in dest:
                        dest.append(nfa_transitions[(n_state, symbol)])

                if dest:
                    for d in dest:
                        for value in d:
                            if value not in f_dest:
                                f_dest.append(value)

                    dfa_transitions[(in_state, symbol)] = f_dest

                    if tuple(f_dest) not in q:
                        q.append(tuple(f_dest))

    for key, value in dfa_transitions.items():
        temp_list = [[key[0], key[1], value]]
        dfa_t_func.extend(temp_list)

    for q_state in q:
        for f_state in data["final"]:
            if f_state in q_state:
                dfa_final.append(q_state)

    dfa = {}
    dfa["states"] = dfa_states
    dfa["letters"] = dfa_letters
    dfa["t_func"] = dfa_t_func
    dfa["start"] = dfa_start
    dfa["final"] = dfa_final

    return dfa

    # output_file = open("tp4/output.json", "w+")
    # json.dump(dfa, output_file, separators=(",\t", ":"))


# Esta func se exporta y se usa en el run()
def validate(path: str, string: str):
    is_valid_string = True
    dfa = initial(path)
    t_func = dfa["t_func"]
    start = str(dfa["start"])
    final = dfa["final"]

    final = ["".join(map(str, tpl)) for tpl in final]

    for state in t_func:
        state[0] = "".join(map(str, state[0]))
        state[2] = "".join(map(str, state[2]))

    i = 0
    next_i = 0
    currentState = start

    while i < len(string):
        for transition in t_func:
            if transition[0] == currentState and transition[1] == None:
                currentState = transition[2]
                i -= 1
                break

            if transition[0] == currentState and string[i] == transition[1]:
                currentState = transition[2]
                next_i += 1
                break

        if i < next_i:
            i = next_i
        else:
            is_valid_string = False
            break

        if i == len(string):
            is_valid_string = currentState in final

    return is_valid_string
