
def merge_the_tools(string, k):
    # your code goes here
    n = len(string)
    i = n / k
    i = int(i)
    t = []
    temp = string
    for j in range(i):
        t.append(temp[:k])
        temp = temp[k:]

    ou = ["".join(dict.fromkeys(u)) for u in t]
    print(*ou, sep='\n')


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
