N, K, P, T = map(int, input().split())
hand = [tuple(map(int, input().split())) for _ in range(T)]

remain = [0]*(N+1)
remain[P] = K
ans = [0]*(N+1)
ans[P] = 1

hand.sort(key = lambda x:(x[0]))

for ti,xi,yi in hand:
    if ans[xi] == 1 and ans[yi] == 1:
        remain[xi] -= 1
        remain[yi] -= 1
        continue
    if ans[xi] == 1 and remain[xi] >0 and ans[yi] == 0:
        ans[yi] = 1
        remain[yi] = K
        remain[xi] -= 1
    elif ans[yi] == 1 and remain[yi] >0 and ans[xi] == 0:
        ans[xi] = 1
        remain[xi] = K
        remain[yi] -= 1         
for i in ans[1:]:
    print(i,end="")
