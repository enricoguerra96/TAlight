#!/usr/bin/python
from sys import stderr, exit, argv

while True:
    spoon = input().strip()
    while spoon[0] == '#':
        spoon = input().strip()
    T = spoon.split()
    spoon = input().strip()
    while spoon[0] == '#':
        spoon = input().strip()
    S = spoon.split()
    pos_S = 0
    indexes = []
    for wanted, i in zip(T,range(len(T))):

        if S[pos_S] == wanted:
            pos_S += 1
            indexes.append(i)
            if pos_S == len(S):
                print('y')
                break
                if len(argv) == 1:
                    print("#", end=" ")
                print(" ".join(map(str,indexes)))
                

    if pos_S < len(S):
        print('n')
exit(0)