for i in range(int(input())):
    nocubes = int(input())
    cubelengths = list(map(int, input().split()))
    ml = len(cubelengths)

    if len(cubelengths) == nocubes:
        # als
        i = 0
        while i < ml-1 and cubelengths[i] >= cubelengths[i+1]:
            # print(f"{cubelengths[i]} is bigger than {cubelengths[i+1]}")
            i += 1

        while i < ml-1 and cubelengths[i] <= cubelengths[i+1]:
            # print(f"{cubelengths[i]} is smaller than {cubelengths[i+1]}")
            i += 1
        if i == ml -1:
            print("Yes")
        else:
            print("No")
