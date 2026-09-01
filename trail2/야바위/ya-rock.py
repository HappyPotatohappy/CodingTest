import sys
input = sys.stdin.readline

n = int(input())
moves = [tuple(map(int, input().split())) for _ in range(n)]
a, b, c = zip(*moves)
a, b, c = list(a), list(b), list(c)
mx = -sys.maxsize
for i in range(1,4):
    cup = [0]*(4)
    cup[i] = 1
    sc = 0
    for ai,bi,ci in zip(a,b,c):
        cup[ai], cup[bi] = cup[bi], cup[ai]
        if cup[ci] == 1:
            sc +=1
    mx = max(sc,mx)

sys.stdout.write(str(mx))