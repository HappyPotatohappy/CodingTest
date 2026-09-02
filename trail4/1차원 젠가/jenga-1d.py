n = int(input())
blocks = [int(input()) for _ in range(n)]
s1, e1 = map(int, input().split())
s2, e2 = map(int, input().split())
tmp1 = []
for i in range(n):
    if s1-1 <= i <= e1-1:
        continue
    tmp1.append(blocks[i])

n2 = len(tmp1)
tmp2 = []
for j in range(n2):
    if s2-1 <= j <= e2 -1:
        continue
    tmp2.append(tmp1[j])


print(len(tmp2))
for i in tmp2:
    print(i)