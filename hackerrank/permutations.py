from itertools  import permutations

def get_perm():
    p_string, p_length = input().split()
    for _ in sorted(list(permutations(p_string, int(p_length)))):
        print(*_, sep="")


get_perm()