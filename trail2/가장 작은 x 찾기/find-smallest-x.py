import sys
input = sys.stdin.readline

n = int(input())
ranges = [tuple(map(int, input().split())) for _ in range(n)]
a, b = zip(*ranges)
a, b = list(a), list(b)
a.insert(0,0)
b.insert(0,0)
mn = sys.maxsize

for x in range(1,10001):
    tmp = 0
    for i in range(1,n+1):
        ai = a[i]
        bi = b[i]
        if ai<= x*2**i and bi>= x*2**i:
            tmp +=1
    if tmp == n:
        mn = min(mn,x)
sys.stdout.write(str(mn))
    
    