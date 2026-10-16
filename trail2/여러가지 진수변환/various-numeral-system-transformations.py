N, B = map(int, input().split())

tmp = []
while N:
    tmp.append(N%B)
    N = N//B

a = len(tmp)
for i in range(len(tmp)):
    print(tmp[a-i-1],end='')