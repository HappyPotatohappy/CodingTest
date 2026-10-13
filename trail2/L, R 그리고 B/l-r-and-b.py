board = [list(input()) for _ in range(10)]

strg = []

for i in range(10):
    for j in range(10):
        if board[i][j] != ".":
            strg.append([board[i][j],i,j])

strg.sort()

start_r = strg[1][1]
start_c = strg[1][2]

end_r = strg[0][1]
end_c = strg[0][2]

bar_r = strg[2][1]
bar_c = strg[2][2]

if (bar_r == start_r == end_r and (start_c <= bar_c <= end_c or end_c <= bar_c <= start_c ) )or (bar_c == start_c == end_c and (start_r <= bar_r <= end_r or end_r <= bar_r <= start_r )):
    ans = abs(start_r - end_r) + abs(start_c - end_c) - 1 + 2
else:
    ans = abs(start_r - end_r) + abs(start_c - end_c) - 1 
print(ans)