#!/bin/python3


def drawDoormat(n, m):
    pattern = ".|."
    filling = "-"
    odds = [ i for i in range(n) if (i % 2) != 0]
    for i in odds:
        print((pattern*i).center(m, filling))

    print("WELCOME".center(m, filling))
    odds.reverse()
    for i in odds:
        print((pattern*i).center(m, filling))


if __name__ == "__main__":
    nm = input().split()
    n = int(nm[0])
    m = int(nm[1])
    drawDoormat(n, m)
