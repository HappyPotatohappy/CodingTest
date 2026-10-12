n = int(input())
a = list(map(int, input().split()))

check = 0

for i in range(n):
    if i and a[i-1] != a[i]:
        check = 1
        break
b = a[:]
b.sort()
b = set(b)
b = list(b)
if len(b) != 1:
    tmp = b[1]
    cnt = 0
    for i in range(n):
        if tmp == a[i]:
            cnt+=1
if check == 0 or cnt >= 2:
    print(-1)
else:
    idx = a.index(tmp)
    print(idx+1)