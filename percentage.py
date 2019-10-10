if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    def query_names(query):
        global student_marks
        return sum(student_marks[query]) / 3

    print(f"{query_names(query_name):.2f}")