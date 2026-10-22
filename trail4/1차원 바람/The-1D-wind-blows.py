n, m, q = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
winds = [(int(r), d) for r, d in [input().split() for _ in range(q)]]

def push_right(lst):
    tmp = lst[0]
    for i in range(m-1):
        lst[i] = lst[i+1]
    lst[m-1] = tmp

def push_left(lst):
    tmp = lst[m-1]
    for i in range(m-1):
        lst[m -i -1] = lst[m -i - 2]
    lst[0] = tmp

def check_common(lst1,lst2):
    for i in range(m):
        if lst1[i] == lst2[i]:
            return 1
    return 0

def in_range(nx):
    return 0 <= nx <= n-1

dTonum = {"L": 0, "R": 1}

for i in range(q):
    now = winds[i][0] - 1
    di = dTonum[winds[i][1]]
    if di == 0:
        push_left(a[now])
    else:
        push_right(a[now])
    nx1 = now + 1
    nx2 = now - 1
    tmp1 = now
    tmp2 = now
    di_nxt = di
    for j in range(n):
        di_nxt = (di_nxt + 1)%2
        if in_range(nx1) and check_common(a[tmp1],a[nx1]):
            if di_nxt == 0:
                push_left(a[nx1])
            else:
                push_right(a[nx1])
            tmp1 = nx1
            nx1 = nx1 + 1
        if in_range(nx2) and check_common(a[tmp2],a[nx2]):
            if di_nxt == 0:
                push_left(a[nx2])
            else:
                push_right(a[nx2])
            tmp2 = nx2
            nx2 = nx2 - 1

for i in a:
    print(*i)
