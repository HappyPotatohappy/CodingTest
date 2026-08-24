import sys
input = sys.stdin.readline

n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]
num = [0]*(101)

for st,ed in segments:
    for i in range(st,ed+1):
        num[i] +=1
mx = max(num)

sys.stdout.write(str(mx))