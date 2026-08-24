import sys
input = sys.stdin.readline
n = int(input())
x = []
dir = []
num = [0]*(2001)
now = 1000
for _ in range(n):
    xi, di = input().split()
    x.append(int(xi))
    dir.append(di)
    if di == "R":
        st = now
        ed = now + int(xi)
        now = ed 
    else:
        st = now - int(xi)
        ed = now
        now = st
    for i in range(st,ed):
        num[i] +=1

cnt = 0
for i in num:
    if i >=2:
        cnt += 1
sys.stdout.write(str(cnt))

