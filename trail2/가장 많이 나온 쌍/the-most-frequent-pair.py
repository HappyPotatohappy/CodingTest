import sys
input = sys.stdin.readline

n, m = map(int, input().split())
pairs = [tuple(map(int, input().split())) for _ in range(m)]
new = []
cnt = {}
for i in pairs:
    new.append(sorted(i))

mx = -sys.maxsize

for i in new:
    key = tuple(i)
    if key not in cnt:
        cnt[key] = 1
    else:
        cnt[key] +=1
    mx = max(mx,cnt[key])

sys.stdout.write(str(mx))
