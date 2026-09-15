import sys
n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]

mn = sys.maxsize

for i in range(1,n-1):## i는 뺼 점
    tmp = 0
    for j in range(1,n):
        if i == j:
            tmp += (abs(x[i-1]-x[j+1]) + abs(y[i-1] - y[j+1]) - abs(x[i]-x[i+1]) - abs(y[i]-y[i+1]))
            continue
        tmp += (abs(x[j-1] - x[j]) + abs(y[j-1] - y[j]))
    mn = min(tmp,mn)
print(mn)