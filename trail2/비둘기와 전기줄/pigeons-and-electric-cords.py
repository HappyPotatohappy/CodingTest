import random
N = int(input())
t = []
for _ in range(N):
    p, pos = map(int, input().split())
    t.append([p,pos])

t.sort(key = lambda x: x[0])
cnt = 0
for i in range(N-1):
    pi = t[i][0]
    xi = t[i][1]
    p_nxt = t[i+1][0]
    x_nxt = t[i+1][1]
    if pi == p_nxt and xi != x_nxt:
        cnt += 1
print(cnt)

