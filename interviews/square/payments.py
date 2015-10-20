class payment_config:

    def __init__(self, payment_states, start_state, valid_transitions):
        self.payment_states = payment_states
        self.start_state = start_state
        self.valid_transitions = valid_transitions

    def validate(self, sequence):
        if sequence[0] != start_state: return False
        for i in range(len(sequence) - 1):
            if sequence[i] not in self.valid_transitions or sequence[i + 1] not in self.valid_transitions[sequence[i]]:
                return False
        return True

    def loop(self, adjacents, sequence):
        for a in adjacents:
            if a in sequence:
                return a
        return None

    def reorder(self, sequence):
        if self.start_state not in sequence: return None
        visited = [start_state]
        while len(visited) < len(sequence):
            cur = visited[-1]
            adjacents = self.valid_transitions[cur]
            next_state = self.loop(adjacents, sequence)
            if next_state: visited.append(next_state)
            else: return None
        return visited

payment_states = ['A', 'C', 'R', 'V']
start_state = 'A'
valid_transitions = {'A': set(['C', 'V']), 'C': set(['R'])}
sequence_a = ['A', 'C', 'R']
sequence_b = ['A', 'V', 'R']
sequence_c = ['V', 'R']
sequence_d = []
a = payment_config(payment_states, start_state, valid_transitions)
print(a.validate(sequence_a))
print(a.validate(sequence_b))
print(a.validate(sequence_c))

wrong_sequence_a = ['C', 'A', 'R']
print(a.reorder(wrong_sequence_a))
