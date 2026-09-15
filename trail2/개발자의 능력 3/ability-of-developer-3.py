import sys
abl = list(map(int, input().split()))
tabl = sum(abl)
mn = sys.maxsize
for i in range(6):
    for j in range(i+1,6):
        for k in range(j+1,6):
            tmp1 = abl[i] + abl[j] +abl[k]
            tmp2 = tabl - tmp1
            mn = min(mn,abs(tmp1-tmp2))
print(mn)

