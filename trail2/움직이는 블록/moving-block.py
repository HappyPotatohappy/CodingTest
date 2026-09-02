n = int(input())
blocks = [int(input()) for _ in range(n)]

goal = sum(blocks)//n
cnt = 0
for i in blocks:
    if i > goal:
        cnt += i - goal
    
print(cnt)