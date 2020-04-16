###########################
# Functions in python
# --------------------
# Notes from the tutorial session
#
#
#############################


def f(x):
    """
    This function will
    take in input, and
    square it.
    """
    return x ** 2


f1 = f(100)
f2 = f(50)

print('f1 =', f1, 'f2 =', f2)
print(f.__doc__)


def greater_than(x, y):
    if x > y:
        return x
    else:
        return y


g1 = greater_than(10, 5)
g2 = greater_than(100, 200)
print(g1)
print(g2)


def unlimited(*args):
    for x in args:
        print(x)

u1 = unlimited(1, 2, 3, 4, 5, 6)


def average(*args):
    sum = 0
    y = len(args)
    for x in args:
        sum += x
    return sum / y


a1 = average(100, 90, 80)
print(a1)

# keyword argument


def g(x=10):
    return x * 10


print(g())
print(g(100))