import sys
input = sys.stdin.readline

x1 = [0] * 3
y1 = [0] * 3
x2 = [0] * 3
y2 = [0] * 3

grp = [[0]*2001 for _ in range(2001)]
x1[0], y1[0], x2[0], y2[0] = map(int, input().split())
x1[1], y1[1], x2[1], y2[1] = map(int, input().split())
#x1[2], y1[2], x2[2], y2[2] = map(int, input().split())

for a,b,c,d in zip(x1,y1,x2,y2):
    for i in range(a,c):
        for j in range(b,d):
            grp[i][j] = 1

a,b,c,d = map(int, input().split())

for i in range(a,c):
    for j in range(b,d):
        grp[i][j] = 0
s = 0
for i in grp:
    s += sum(i)
sys.stdout.write(str(s))