import sys
input = sys.stdin.readline

INT_MAX = sys.maxsize
INT_MIN = -sys.maxsize

n = int(input())
h = list(map(int,input().split()))
min_sum = INT_MAX

for i in range(n):
    now = i
    tmp = 0
    for j in range(n):
        if j == i:
            continue
        leng = abs(i - j)
        tmp += leng*h[j]
    if tmp < min_sum:
        min_sum = tmp

sys.stdout.write(str(min_sum))