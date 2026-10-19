n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]


def check_lst(lst):
    is_true = 0
    cnt = 0 
    for i in range(1,n):
        if lst[i-1] == lst[i]:
            cnt += 1
        if lst[i-1] != lst[i]:
            cnt = 0
            continue
        if cnt == m - 1:
            is_true = 1
            break
    
    return is_true

def get_col(grid):
    ans = []
    for i in range(n):
        tmp = []
        for j in range(n):
            tmp.append(grid[j][i])
        ans.append(tmp)
    return ans

if m == 1:
    print(2*n)
else:
    ans = 0
    grid2 = get_col(grid)
    for i in range(n):
        a = check_lst(grid[i])
        b = check_lst(grid2[i])
        ans = ans + a + b
    print(ans)