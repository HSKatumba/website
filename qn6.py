import math

c = 50

h = 30

value = []

items = [x for x in input().split(",")]

def sroot_sequence():
    for d in items:
        value.append(str(int(math.sqrt((2*c*int(d))/h))))
    print(value)
