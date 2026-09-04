import sys
n, k = map(int, input().split())
cand = []
ps = []

for _ in range(n):
    c, p = map(int, input().split())
    cand.append(c)
    ps.append(p)


## c-k = 0 c+k = n-1
mx = -1
up = min(n,n-k)
now = 0
ps_max = max(ps)
while 1:
    st = max(0,now - k)
    ed = now + k
    tmp = 0
    for i in range(n):
        if st <= ps[i] <=ed:
            tmp += cand[i]
    mx = max(mx,tmp)
    now += 1

    if  now  >= ps_max:
        break

print(mx)