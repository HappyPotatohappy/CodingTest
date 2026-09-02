n, t = map(int, input().split())
u = list(map(int, input().split()))
d = list(map(int, input().split()))


for _ in range(t):
    if n == 1:
        u[0],d[0] = d[0], u[0]
    else:
        tmpUp = u[-1]
        tmpDown = d[-1]
        i = n - 1
        while 1:
            u[i] = u[i-1]
            d[i] = d[i-1]
            i -= 1
            if i == 0:
                break
        u[0] = tmpDown
        d[0] = tmpUp


print(*u)
print(*d)