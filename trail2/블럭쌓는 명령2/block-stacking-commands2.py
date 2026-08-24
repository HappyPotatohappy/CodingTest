import sys
input = sys.stdin.readline

n,k = map(int,input().split())

block = [0]*(n+1)

for i in range(k):
    a,b = map(int,input().split())
    for j in range(a,b+1):
        block[j] +=1
mx = max(block)
sys.stdout.write(str(mx))