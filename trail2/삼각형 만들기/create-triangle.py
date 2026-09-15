n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]
mx = 0
for i in range(n):
    nowx = x[i]
    nowy = y[i]
    mx_lenx = 0
    mx_leny = 0
    for j in range(n):
        if i==j:
            continue
        if x[j] == nowx:
            mx_leny = max(mx_leny,abs(nowy-y[j]))
        if y[j] == nowy:
            mx_lenx = max(mx_lenx,abs(nowx-x[j]))
    mx = max(mx,mx_lenx*mx_leny)
print(mx)