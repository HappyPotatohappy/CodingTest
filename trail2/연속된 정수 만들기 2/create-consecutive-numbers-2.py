import sys
input = sys.stdin.readline
pos = list(map(int, input().split()))

pos.sort()
p1,p2,p3 = pos[0],pos[1],pos[2]

d1 = p2 - p1
d2 = p3 - p2

if d1 == 1 and d2 ==1:
    sys.stdout.write(str(0))
elif d1==2 or d2==2:
    sys.stdout.write(str(1))
else:
    sys.stdout.write(str(2))