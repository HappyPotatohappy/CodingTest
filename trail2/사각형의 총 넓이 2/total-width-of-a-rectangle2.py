import sys
input = sys.stdin.readline
n = int(input())
x1, y1, x2, y2 = [], [], [], []
for _ in range(n):
    a, b, c, d = map(int, input().split())
    x1.append(a+100)
    y1.append(b+100)
    x2.append(c+100)
    y2.append(d+100)

grp = [[0]*201 for _ in range(201)]

for x_1,y_1,x_2,y_2 in zip(x1,y1,x2,y2):
    for i in range(x_1,x_2):
        for j in range(y_1,y_2):
            grp[i][j] = 1

s = 0
for i in grp:
    s += sum(i)
sys.stdout.write(str(s))
