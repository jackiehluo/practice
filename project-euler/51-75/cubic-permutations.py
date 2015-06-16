cubes = {}
for i in xrange(10000):
    n = i ** 3
    perm = "".join(sorted(str(n)))
    if perm in cubes:
        cubes[perm].append(n)
        if len(cubes[perm]) == 5:
            print min(cubes[perm])
            break
    else:
        cubes[perm] = [n]
