import sys
input = sys.stdin.readline

n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

line = [0]*(201)

for st,ed in segments:
    st += 100
    ed += 100
    for i in range(st,ed):
        line[i] +=1

mx = max(line)

sys.stdout.write(str(mx))