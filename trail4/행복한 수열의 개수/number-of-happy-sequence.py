n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

cnt = 0

def check(numlist):
    cnt = 0
    for i in range(1,n):
        if numlist[i-1] != numlist[i]:
            cnt = 0
            continue
        if numlist[i-1] == numlist[i]:
            cnt+=1
        if cnt == m - 1:
            return 1
    if cnt >= m - 1:
        return 1
    return 0
ans = 0

for i in range(n):
    row = grid[i]
    col = [row[i] for row in grid]
    ans += check(col)
    ans += check(row)
print(ans)