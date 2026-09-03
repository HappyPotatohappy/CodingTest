n, m, t = map(int, input().split())

# Create n x n grid
a = [list(map(int, input().split())) for _ in range(n)]

# Get m marble positions
marbles = [tuple(map(int, input().split())) for _ in range(m)]
r = [pos[0] for pos in marbles]
c = [pos[1] for pos in marbles]
tmp = [0]*(n+2)
for i in a:
    i.append(0)
    i.insert(0,0)
a.append(tmp)
a.insert(0,tmp)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def check_range(nx,ny):
    if 1 <= nx <= n and 1 <= ny <= n:
        return 1
    else:
        return 0

def move_and_check(r,c):#한번의 이동 후 r,c의 리스트 => 없어지는 구슬까지 체크해서 반환
    newGrid = [[0]*(n+2) for _ in range(n+2)]

    for i,j in zip(r,c):
        mx = -1
        dir = -1

        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]
            if check_range(nx,ny) and mx < a[nx][ny]:
                dir = k
                mx = a[nx][ny]
        newGrid[i+dx[dir]][j+dy[dir]]+=1

    new_r=[]
    new_c=[]

    for i in range(1,n+1):
        for j in range(1,n+1):
            if newGrid[i][j] >= 2:
                newGrid[i][j] = 0
            if newGrid[i][j] == 1:
                new_r.append(i)
                new_c.append(j)

    return new_r,new_c

    
for _ in range(t):
    r,c = move_and_check(r,c)

print(len(r))