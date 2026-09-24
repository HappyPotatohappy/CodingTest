import random
n = int(input())
moves = [tuple(map(int, input().split())) for _ in range(n)]
a, b, c = zip(*moves)
a, b, c = list(a), list(b), list(c)
sc = 0
for i in range(1,4): ## 어디에 돌을 넣을지 모두 탐색
    cnt = 0
    cup = [0]*4
    cup[i] = 1
    for j in range(n):
        cup[a[j]], cup[b[j]] = cup[b[j]], cup[a[j]]
        if cup[c[j]] == 1:
            cnt +=1
    sc = max(cnt,sc)

print(sc)