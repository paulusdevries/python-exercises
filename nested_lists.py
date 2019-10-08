if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])

    second = []
    low = min(students, key=lambda x: x[1])

    for _ in range(len(students)):
        if students[_][1] > low[1]:
            second.append(students[_])

    again = []
    second_low = min(second, key=lambda x: x[1])
    again.append(second_low)
    for _ in range(len(second)):
        if second[_][1] == second_low[1] and second[_] != second_low:
            again.append(second[_])

    again = sorted(again)
    for _ in range(len(again)):
        print(again[_][0])