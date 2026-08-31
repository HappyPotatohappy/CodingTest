import sys
input = sys.stdin.readline

abl = list(map(int, input().split()))
total_abl = sum(abl)

mn = sys.maxsize

for i in range(6):
    for j in range(6):
        for k in range(6):
            if i==j or j==k or i==k:
                continue
            t1 = abl[i] + abl[j] + abl[k]
            t2 = total_abl - t1
            mn = min(mn,abs(t1-t2))

sys.stdout.write(str(mn))