if __name__ == '__main__':
    N = int(input())
    command = []
    list_ = []
    for i in range(N):
        command = list(input().split())
        if command[0] == "insert":
            list_.insert(int(command[1]), int(command[2]))
        if command[0] == "reverse":
            list_.reverse()
        if command[0] == "append":
            list_.append(int(command[1]))
        if command[0] == "sort":
            list_.sort(key=int)
        if command[0] == "pop":
            list_.pop()
        if command[0] == "remove":
            list_.remove(int(command[1]))
        if command[0] == "print":
            print(list_)

