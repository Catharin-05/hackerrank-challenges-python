from collections import defaultdict

def get_indices():
    n, m = map(int, input().strip().split())
    d = defaultdict(list)

    for i in range(n):
        elem = input().strip()
        d[elem].append(i+1)
    for j in range(m):
        elemB = input().strip()
        if elemB in d:
            print(*d[elemB])
        else:
            print(-1)
get_indices()
