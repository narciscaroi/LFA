import sys


def check_language(language, string):
    # pentru fiecare litera din alfabet
    for i in language:
        # verific daca este acceasi cu cea pe care vrem sa o introducem
        if string == i:
            return 0
    return 1


def state_exist_in_eps(eps_transitions, j):
    for i in eps_transitions:
        if i == str(j):
            return 1
    return 0


def epsilon_closure(eps_transitions, states_number):
    clos = {}
    queue = []
    # pentru fiecare stare
    for i in range(0, states_number):
        clos[str(i)] = set()
        clos[str(i)].add(i)
        # verific daca aceasta are o epsilon-tranzitie directa
        if state_exist_in_eps(eps_transitions, i) == 0:
            continue
        # concatenez in coada fiecare epsilon-tranzitie directa pe care o are starea
        for j in range(0, len(eps_transitions[str(i)])):
            queue.append(eps_transitions[str(i)][j])

        for j in queue:
            # verific daca fiecare stare din coada are o alta epsilon-tranzitie
            if state_exist_in_eps(eps_transitions, j) == 1:
                for k in eps_transitions[str(j)]:
                    # verific sa nu fie deja in que sau in lista de tranzitii pentru starea curenta
                    if k not in queue and k not in clos[str(i)]:
                        queue.append(k)

        for j in range(0, len(queue)):
            # pun elementele din coada in lista pentru starea curenta
            clos[str(i)].add(queue.pop(0))
        queue.clear()
    return clos


def calculate_tranzition(nfa_delta, ecloser, automata_language, queue):
    lista = {}
    # initializare
    for j in automata_language:
        if j != "eps":
            lista[j] = set()

    for i in queue:
        # verificare sink_state notat cu -1
        if i < 0:
            continue
        for j in automata_language:
            if j == "eps":
                continue
            if j in nfa_delta[i]:
                for k in nfa_delta[i][j]:
                    # verific daca exista tranzitie si o adaug
                    if k not in lista[j]:
                        lista[j].add(k)
                        # verific tranzitiile din epsilon_closure
                        for e in ecloser[str(k)]:
                            if e not in lista[j]:
                                lista[j].add(e)
    for j in automata_language:
        if j == "eps":
            continue
        # adaug sink_state
        if len(lista[j]) == 0:
            lista[j].add(-1)
    return lista


def get_dfa_delta_index(covered_states, listaj):
    idx = 0
    for i in covered_states:
        if i == listaj:
            return idx
        idx += 1
    return -1


def get_dfa_delta_lindex(covered_states, queue, delta_indexes):
    counter = 0
    for i in covered_states:
        if i == queue:
            return delta_indexes[counter]
        counter += 1
    return 0


def check_exist_final_state_initial(final_states, lista):
    for i in final_states:
        if i in lista[0]:
            return 1
    return 0


def check_exist_final_state(final_states, lista, j):
    for i in final_states:
        for k in lista[j]:
            if k == i:
                return 1
    return 0


def compute_dfa_delta(nfa_delta, automata_language, final_states, ecloser, dfa_final_states):
    dfa_delta = {}
    delta_idx = 0
    # initializez coada, starile acoperite si index-ul starii initiale si counter-ul pentru index
    queue = [ecloser['0']]
    covered_states = [ecloser['0']]
    delta_indexes = [0]
    counter = 1
    # verific daca initial trebuie sa adaug stare finala
    if check_exist_final_state_initial(final_states, covered_states):
        dfa_final_states.append(0)
    # cat timp am elemente in coada
    while queue:
        # calculez lista de tranzitii
        lista = calculate_tranzition(nfa_delta, ecloser, automata_language, queue[0])
        dfa_delta[delta_idx] = {}
        for i in automata_language:
            if i == "eps":
                continue
            dfa_delta[delta_idx][i] = {}
            # daca lista pe un caracter nu este in starile acoperite
            if lista[i] not in covered_states:
                covered_states.append(lista[i])
                delta_indexes.append(counter)
                if check_exist_final_state(final_states, lista, i):
                    dfa_final_states.append(counter)
                queue.append(lista[i])
                counter += 1
            # adaug elementele din lista de tranzitii in tabelul pentru dfa
            for i in automata_language:
                if i == "eps":
                    continue
                idx_l = get_dfa_delta_lindex(covered_states, queue[0], delta_indexes)
                idx_col = get_dfa_delta_index(covered_states, lista[i])
                dfa_delta[idx_l][i] = idx_col
        delta_idx += 1
        queue.pop(0)
    return  dfa_delta


if __name__ == '__main__':
    nfa_delta = {}
    f = open(sys.argv[1], "r")
    states_number = int(f.readline().rstrip('\n'))
    final_states = ([int(x) for x in f.readline().rstrip('\n').split()])

    for i in range(0, states_number):
        nfa_delta[i] = {}

    automata_language = []
    eps_transitions = {}
    for line in f:
        line = line.rstrip('\n').split(' ')
        nfa_delta[int(line[0])][str(line[1])] = ([int(x) for x in line[2:]])
        if check_language(automata_language, line[1]) == 1:
            automata_language.append(str(line[1]))
        if line[1] == "eps":
            eps_transitions[line[0]] = nfa_delta[int(line[0])][str(line[1])]

    f.close()

    automata_language.sort()
    ecloser = epsilon_closure(eps_transitions, states_number)
    dfa_final_states = []
    dfa_delta = compute_dfa_delta(nfa_delta, automata_language, final_states, ecloser, dfa_final_states)

    f = open(sys.argv[2], "w")
    f.write(str(len(dfa_delta)))
    f.write('\n')
    for i in dfa_final_states:
        f.write(str(i))
        f.write(" ")
    f.write('\n')
    for i in range(0, len(dfa_delta)):
        for j in automata_language:
            if j == "eps":
                continue
            f.write(str(i))
            f.write(" ")
            f.write(str(j))
            f.write(" ")
            f.write(str(dfa_delta[i][j]))
            f.write('\n')
    f.close()