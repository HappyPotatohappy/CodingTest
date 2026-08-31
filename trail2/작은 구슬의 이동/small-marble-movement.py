import sys
input = sys.stdin.readline
n, t = map(int, input().split())
r, c, d = input().split()
r, c = int(r), int(c)
altoNum = {"U": 1, "D": 2, "R":0,"L":3}
dx = [0,-1,1,0]
dy = [1,0,0,-1] 
## 이렇가 하면 3-now 면 방향을 반대로 바꾼다!
## 다음칸이 0 이면 dir = 3 - dir 로 만들면 되겠다.
## 시간 관리는 T -= 1 이걸로 해보자.

tmp = [0]*(n+2)
grp = [[1]*n for _ in range(n)]
for i in grp:
    i.append(0)
    i.insert(0,0)
grp.append(tmp)
grp.insert(0,tmp)

now_x = r
now_y = c    
dir = altoNum[d]
while t:
    nx = now_x + dx[dir]
    ny = now_y + dy[dir]
    if grp[nx][ny]:
        t = t - 1
        now_x = nx
        now_y = ny
    else:
        dir = 3 - dir
        t = t - 1

sys.stdout.write(str(now_x) + " " + str(now_y))
