from math import sqrt

def complex_print(n):
    if not n.real == 0 and not n.imag == 0:
        if n.imag > 0:
            print format(n.real, '.2f'), "+", format(n.imag, '.2f') + "i"
        else:
            print format(n.real, '.2f'), "-", format(abs(n.imag), '.2f') + "i"
    elif not n.real == 0:
        print format(n.real, '.2f')
    elif not n.imag == 0:
        print format(n.imag, '.2f') + "i"
    else:
        print format(0, '.2f')

a, ai = map(float, raw_input().split())
b, bi = map(float, raw_input().split())
ca = complex(a, ai)
cb = complex(b, bi)

complex_print(ca + cb)
complex_print(ca - cb)
complex_print(ca * cb)
complex_print(ca / cb)
print format(sqrt(a ** 2 + ai ** 2), '.2f')
print format(sqrt(b ** 2 + bi ** 2), '.2f')