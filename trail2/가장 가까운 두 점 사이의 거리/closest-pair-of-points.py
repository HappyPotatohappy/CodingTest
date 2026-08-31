import sys
input = sys.stdin.readline
n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]

mn = sys.maxsize

for i in range(n):
    for j in range(n):
        if i==j:
            continue
        l = (x[i] - x[j])**2 + (y[i] - y[j])**2
        mn = min(l,mn)

sys.stdout.write(str(mn))