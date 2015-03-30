from collections import Counter

def check(message, text):
    m_counts = Counter(message)
    t_counts = {}
    for c in text:
        if c in m_counts:
            if c in t_counts:
                t_counts[c] += 1
            else:
                t_counts[c] = 1
            if t_counts[c] == m_counts[c]:
                    m_counts.pop(c, None)
                    if not m_counts:
                        return True
    return False

message = raw_input()
text = raw_input()
print check(message, text)