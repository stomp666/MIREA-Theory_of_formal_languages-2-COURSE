class FA:
    def __init__(self, states, alphabet, transitions, initial, final):
        self.states = states
        self.alphabet = alphabet
        self.transitions = transitions
        self.initial = initial
        self.final = final

def nfa_to_dfa(nfa):
    dfa_states = set()
    dfa_transitions = {}
    dfa_initial = tuple(nfa.initial)
    dfa_final = set()

    queue = [dfa_initial]
    while queue:
        current_state = queue.pop(0)
        dfa_states.add(current_state)

        for symbol in nfa.alphabet:
            next_state = set()
            for state in current_state:
                next_state.update(nfa.transitions.get((state, symbol), set()))
            next_state = tuple(sorted(next_state))

            dfa_transitions[(current_state, symbol)] = next_state
            if next_state not in queue and next_state not in dfa_states:
                queue.append(next_state)

        if any(state in nfa.final for state in current_state):
            dfa_final.add(current_state)

    return FA(dfa_states, nfa.alphabet, dfa_transitions, dfa_initial, dfa_final)



def main():
    transitions = {
        ('1', 'a'): {'1', '2'},
        ('1', 'b'): {'3'},
        ('2', 'a'): {'2'},
        ('2', 'b'): {'1', '3'},
        ('3', 'a'): {'3'},
        ('3', 'b'): {'3'},
    }
    nfa = FA({'1', '2', '3'}, {'a', 'b'}, transitions, {'1'}, {'3'})
    dfa = nfa_to_dfa(nfa)
    # Nondeterministic finite automaton 2 Deterministic finite automaton

    print("Deterministic finite automaton:")
    print("States:", dfa.states)
    print("Alphabet:", dfa.alphabet)
    print("Transitions:")
    for (state, symbol), next_state in dfa.transitions.items():
        print(f"D({state}, {symbol}) = {next_state}")
    print("Initial state:", dfa.initial)
    print("Final states:", dfa.final)

if __name__ == "__main__":
    main()
