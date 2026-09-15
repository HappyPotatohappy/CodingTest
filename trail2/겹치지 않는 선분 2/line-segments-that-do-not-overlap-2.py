n = int(input())
lines = [tuple(map(int, input().split())) for _ in range(n)]

cnt = 0
for i in range(n):
    now1 = lines[i][0]
    now2 = lines[i][1]
    tmp1 = 0
    for j in range(n):
        if i ==j:
            continue
        new1 = lines[j][0]
        new2 = lines[j][1]
        if (now1 - new1)*(now2 - new2) >0:
            tmp1 +=1
    if tmp1 == n-1:
        cnt+=1

print(cnt)