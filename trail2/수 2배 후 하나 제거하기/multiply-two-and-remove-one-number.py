import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

sc = sys.maxsize
for i in range(n):
    

    for j in range(n):
        cop = arr[:]
        cop[i]*=2
        cop.pop(j)
        s = 0

        for k in range(n-2):
            s += abs(cop[k] - cop[k+1])
        sc = min(sc,s)

sys.stdout.write(str(sc))