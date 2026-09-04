n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

def find(num_list):
    cnt_same = 0
    for i in range(1,n):
        if num_list[i] == num_list[i-1]:
            cnt_same +=1
            if cnt_same == m -1:
                return 1
        elif num_list[i] != num_list[i-1]:
            cnt_same = 0
    return 0
        
cnt = 0
for i in range(n):
    tmp = grid[i]
    tmp2 = [col[i] for col in grid]
    if find(tmp):
        cnt +=1
    if find(tmp2):
        cnt +=1
if m==1:
    print(2*n)
else:
    print(cnt)