from collections import Counter


def count_shoes():
    shoes = input()
    sizes = list(input().split(sep=" "))
    clients = int(input())
    purchases = []
    earnings = []
    for _ in range(clients):
        purchases.append(input().split())

    for purchase in purchases:
        try:
            index = sizes.index(purchase[0])
            sizes.pop(index)
            earnings.append(int(purchase[1]))
        except Exception as e:
            continue
    earn = sum(earnings)
    return earn


print(count_shoes())

