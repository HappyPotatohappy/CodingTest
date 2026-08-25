import sys
input = sys.stdin.readline
nx = 0
ny = 0
dirs = input().strip()

alNum = {"L":-1,"R":1,"F":2}

dx = [1,0,-1,0]
dy = [0,-1,0,1]

dir_num = 3

for i in dirs:
    dirnum = alNum[i]
    if dirnum == 2:
        nx = nx + dx[dir_num]
        ny = ny + dy[dir_num]
    elif dirnum == -1:
        dir_num = (dir_num+3)%4
    else:
        dir_num = (dir_num+1)%4

sys.stdout.write(str(nx) + " " + str(ny))