cases = int(input())
caseresults = [True for case in range(cases)]
cubes = []
sideLengthList = []
topCube = 0
for i in range(cases):
    cube = int(input())
    cubes.append(cube)
    sideLengths = input().split(" ")
    sideLengthList.append(sideLengths)
    if len(sideLengths) > cube:
        del sideLengths[cube:]

choice = True
for i in range(cases):
    deze = sideLengthList[i-1]
    while len(deze) > 1:
        if choice:
            if deze[0] <= deze[(len(deze)-1)] or deze[(len(deze)-1)] <= deze[0]:
                deze.pop(0)
            else:
                caseresults[i-1] = False
                break
        else:
            if deze[0] <= deze[(len(deze)-1)] or deze[(len(deze)-1)] <= deze[0]:
                deze.pop()
            else:
                caseresults[i-1] = False
                break



    if caseresults[(i-1)]:
        print("Yes")
    else:
        print("No")