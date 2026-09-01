import sys
input = sys.stdin.readline

n, m = map(int, input().split())
pairs = [list(map(int, input().split())) for _ in range(m)]
new = []
for i in pairs:
    new.append(sorted(i))
mx = -sys.maxsize
for i in range(m):
    tmp = 1
    for j in range(m):
        if i==j:
            continue
        if new[i] == new[j]:
            tmp +=1
    mx = max(mx,tmp)

sys.stdout.write(str(mx))
