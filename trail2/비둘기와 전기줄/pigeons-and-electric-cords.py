import sys
input = sys.stdin.readline

n = int(input())
pigeon = []
position = []
for _ in range(n):
    p, pos = map(int, input().split())
    pigeon.append(p)
    position.append(pos)

before = [-1]*11
cnt = 0
for i in range(n):
    pi = pigeon[i]
    posi = position[i]
    if before[pi] == -1:
        before[pi] = posi
        continue
    if before[pi] != posi:
        cnt+=1
        before[pi] = posi
    
sys.stdout.write(str(cnt))