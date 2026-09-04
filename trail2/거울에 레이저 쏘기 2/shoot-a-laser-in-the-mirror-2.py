n = int(input())
grid = [list(input()) for _ in range(n)]
k = int(input())

# Please write your code here.
answer = 0
x, y = 0, 0
a = [0,0]   # arrow
if (k-1)//n == 0:
    a = [1,0]
    x = -1
    y = (k-1)%n
elif (k-1)//n == 1:
    a = [0,-1]
    x = (k-1)%n
    y=n
elif (k-1)//n == 2:
    a = [-1,0]
    x = n
    y=(n-1)-(k-1)%n
else:
    a = [0,1]
    x = (n-1)-(k-1)%n
    y=-1

# 시작위치 x, y
# 시작 위치는 x <0 or y<0 or x==n or y==n 가능
while 1:

    nx = x + a[0]
    ny = y + a[1]
    # 밖으로 나가는 조건 - break
    if nx < 0 or ny < 0 or nx >= n or ny >= n:
        break

    answer += 1

    # 거울 조건
    if grid[nx][ny] == '/':
        if a == [-1,0]: a = [0,1]
        elif a == [1,0]: a = [0,-1]
        elif a ==[0,-1]: a = [1,0]
        elif a == [0,1]: a = [-1,0]
    elif grid[nx][ny] == '\\':
        if a == [-1,0]: a = [0,-1]
        elif a == [1,0]: a = [0,1]
        elif a ==[0,-1]: a = [-1,0]
        elif a == [0,1]: a = [1,0]
    # x, y, a 업데이트
    x=nx
    y=ny

print(answer)