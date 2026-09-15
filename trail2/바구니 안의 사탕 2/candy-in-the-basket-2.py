n, k = map(int, input().split())
candy = []
pos = []

for _ in range(n):
    c, p = map(int, input().split())
    candy.append(c)
    pos.append(p)

mx = 0
def in_range(x):
    return 0 <= x <= 100

for x in range(0,101):
    tmp = 0
    for j in range(n):
        p = pos[j]
        c = candy[j]
        if in_range(x) and (x-k <= p <= x+k):
            tmp += c
    mx = max(tmp,mx)
print(mx)
       
