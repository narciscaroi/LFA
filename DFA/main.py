import sys


# citesc pattern-ul din fisier
def read_word_from_file(filename):
    f = open(filename, "r")
    # citesc prima linie si separ \n
    wd = f.readline().rstrip('\n')
    f.close()
    return wd


# citesc textul din fisier
def read_string_from_file(filename):
    f = open(filename, "r")
    iss = f.readline()
    input_s = f.readline().rstrip('\n')
    f.close()
    return input_s


# scriu in fisier
def write_in_file(filname, result):
    f = open(filname, "w+")
    for i in range(0, len(result)):
        f.write(str(result[i]))
        f.write(" ")
    f.write('\n')

    f.close()


def check_is_next(current_state, current_char):
    # verific daca char-ul pe care il analizez din text este chiar urmatorul din pattern (in functie de stare)
    if current_state < len(given_pattern) and chr(current_char + 65) == given_pattern[current_state]:
        return current_state + 1
    return -1


def check_suffix_prefix(given_pattern, current_char, current_state):
    max_next_state = current_state
    # incep de la cea mai mare valoare posibila
    while max_next_state > 0:
        next_state = 0
        # pornesc de la next_state-ul cel mai mare posibil, adica current_state-1 pana la 0
        # si verific daca litera din starea verificata este egala cu cea din starea curenta
        if ord(given_pattern[max_next_state - 1]) == current_char + 65:
            # verific "stare cu stare" pana la cea maxima sa vad unde pot sa ma opresc
            # pentru a avea sufixul = prefixul
            while next_state < max_next_state - 1:
                if given_pattern[current_state - (max_next_state - 1) + next_state] != given_pattern[next_state]:
                    break
                next_state += 1
            if next_state == max_next_state - 1:
                return next_state + 1
        max_next_state -= 1
    next_state = 0
    return next_state


def compute_delta(g_pattern):
    delta = {0: []}
    # A=0, B=1, C=2,...,Z = 25
    # creez prima linie din matrice "epsilon"
    for i in range(0, 26):
        if ord(g_pattern[0]) == i + 65:
            delta[0].append(1)
        else:
            delta[0].append(0)

    current_state = 1
    next_state = 2
    # pentru fiecare grupare de caractere ( reprezentand liniile ex: L, LF, LFA)
    for c in g_pattern:
        # initializez linia din matrice
        delta[current_state] = []
        # verific fiecare caracter in ce stare trece automatul
        for current_char in range(0, 26):
            next_state = check_is_next(current_state, current_char)
            if next_state == -1:
                next_state = check_suffix_prefix(g_pattern, current_char, current_state)
            # pun in matrice next state-ul obitnut
            delta[current_state].append(next_state)
        current_state += 1
        next_state += 1
    return delta


# functia de la curs putin modificata incat sa se plieze
def automata_matcher(given_pattern, given_string):
    q = 0  # starea initiala
    delta = compute_delta(given_pattern)
    result = []
    for i in range(0, len(given_string)):
        q = delta[q][ord(given_string[i]) - 65]
        if q == len(given_pattern):
            result.append(i - (len(given_pattern) - 1))
    return result


if __name__ == '__main__':
    given_pattern = read_word_from_file(sys.argv[1])
    given_string = read_string_from_file(sys.argv[1])
    result = automata_matcher(given_pattern, given_string)
    # print(result)
    write_in_file(sys.argv[2], result)

    # pattern2 = "EZEZ"
    # string2 = "EZEZEZ"
    # result = automata_matcher(pattern2, string2)
    # print(result)
    # write_in_file("testout.txt", result)
