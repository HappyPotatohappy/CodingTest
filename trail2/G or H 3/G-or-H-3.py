import sys
input = sys.stdin.readline


n, k = map(int, input().split())
x = []
c = []
numlist = [0]*(10000+1)
for _ in range(n):
    pos, char = input().split()
    x.append(int(pos))
    c.append(char)
    sc = 0
    if char == "H":
        sc = 2
    else:
        sc = 1
    numlist[int(pos)] = sc 
mx = -sys.maxsize
for i in range(10001 - k + 2):
    mx = max(mx, sum(numlist[i:i+k+1]))

sys.stdout.write(str(mx))