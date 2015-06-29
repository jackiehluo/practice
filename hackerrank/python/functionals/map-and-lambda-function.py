fib = lambda n: n if n < 2 else fib(n - 1) + fib(n - 2)
print [x ** 3 for x in list(map(fib, range(int(raw_input()))))]