n = int(input())
A = list(map(int, input().split()))
A.insert(0,0)
mn = 100*100*100
for i in range(1,n+1):
    tmp = 0
    for j in range(1,n+1):
        if i==j:
            continue
        tmp += A[j]*(abs(i-j))
    mn = min(tmp,mn)
print(mn)