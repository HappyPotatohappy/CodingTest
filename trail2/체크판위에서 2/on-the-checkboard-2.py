r, c = map(int, input().split())
grid = [list(input().split()) for _ in range(r)]
cnt = 0

def jump(nowx,nowy,jump_cnt):
    global cnt
    if nowx == r-1 and nowy == c-1 and jump_cnt == 3:
        cnt+=1
        return
    if jump_cnt >3:
        return

    for i in range(nowx+1,r):
        for j in range(nowy+1,c):
            if grid[nowx][nowy] != grid[i][j]:
                jump(i,j,jump_cnt+1)
    return

jump(0,0,0)
print(cnt)
