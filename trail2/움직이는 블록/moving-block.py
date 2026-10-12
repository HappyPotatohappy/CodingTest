n = int(input())
blocks = [int(input()) for _ in range(n)]
total = sum(blocks)
goal = total//n

ans = 0
for i in range(n):
    ans += abs(goal - blocks[i])
print(ans//2)