def transform(exp):
    postfix = ""
    operators = []
    for i in exp:
        if i.isalpha():
            postfix += i
        elif i == ")":
            postfix += operators.pop()
        elif isOperator(i):
            operators.append(i)
    return postfix

def isOperator(char):
    if char == "+" or char == "-" or char == "*" or char == "/" or char == "^":
        return True
    return False

t = int(raw_input())

for case in range(t):
    exp = raw_input()
    answer = transform(exp)
    print answer
