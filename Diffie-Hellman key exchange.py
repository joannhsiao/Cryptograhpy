#!/bin/env python3

n = input("g, p = ").replace(",", "")
g, p = list(map(int, n.split(" ")))

digit = len(str(p-1))
if digit < 2:
    digit = 2
for i in range(digit):
    print(" ", end='')
print("| ", end='')
for i in range(1, p):
    for j in range(digit-len(str(i))):
        if i == 1:
            continue
        else:
            print(" ", end='')
    print('%s' % i, end=' ')
print()

for j in range(digit):
    print("-", end='')
print("+--", end='')
for i in range(1, p-1):
    for j in range(digit+1):
        print("-", end='')
print()

for a in range(1, p):
    K = []
    for b in range(1, p):
        K.append(str(pow(g, a*b, p)))
    if len(K) != len(set(K)):
        K.append("Bad")
    for i in range(digit-len(str(a))):
        print(" ", end='')
    print("%s|" % a, end='')
    for i in range(len(K)):
        for j in range(digit-len(str(K[i]))):
            print(" ", end='')
        print(str(K[i]), end=' ')
    print()
