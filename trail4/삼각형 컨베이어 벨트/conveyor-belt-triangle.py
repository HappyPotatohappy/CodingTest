n, t = map(int, input().split())

l = list(map(int, input().split()))
r = list(map(int, input().split()))
d = list(map(int, input().split()))

for _ in range(t):
    tmp_l = l[-1]
    tmp_r = r[-1]
    tmp_d = d[-1]
    for i in range(1,n):
        l[n-i] = l[n-i-1]
        r[n-i] = r[n-i-1]
        d[n-i] = d[n-i-1] 
    l[0] = tmp_d
    r[0] = tmp_l
    d[0] = tmp_r

print(*l)
print(*r)
print(*d)