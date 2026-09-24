import random
n = int(input())
arr = list(map(int, input().split()))
sc = 100*100
for i in range(n): ## 2배로 만들 원소
    arr[i] *= 2
    for j in range(n): ##제거할 원소
        cnt = 0
        remain =[elem for idx, elem in enumerate(arr) if j!=idx]

        for k in range(n-2):
            cnt += abs(remain[k] - remain[k+1])

        sc = min(sc,cnt)
    arr[i] = int(arr[i]/2)
print(sc)
