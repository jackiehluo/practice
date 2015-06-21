def decipher(n, k, message):
    a, b = [message[0]], [message[0]]
    for i in range(1, len(message) - k + 1):
        xor = a[-1] ^ message[i]
        if len(a) >= k:
            b.append(a[-k] ^ xor)
        else:
            b.append(xor)
        a.append(a[-1] ^ b[-1])
    return b

n, k = (int(x) for x in raw_input().split())
message = [int(char) for char in raw_input()]
answer = decipher(n, k, message)
print "".join(map(str, answer))
