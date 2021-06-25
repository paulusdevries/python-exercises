from itertools import product
knm = list(map(int, input().strip().split()))
k = knm[0]
m = knm[1]
n = [list(map(int, input().strip().split())) for num in range(k)]
squares = [[res**2 for res in num[1:]] for num in n]
print(max(map(lambda x: sum(i for i in x) % m, product(*squares))))
