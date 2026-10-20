n, t = map(int, input().split())
u = list(map(int, input().split()))
d = list(map(int, input().split()))


def push_one(lst):
    for i in range(n-1,0,-1):
        lst[i] = lst[i-1]

for _ in range(t):
    tmp_u = u[-1]
    tmp_d = d[-1]
    push_one(u)
    push_one(d)
    u[0] = tmp_d
    d[0] = tmp_u

print(*u)
print(*d)