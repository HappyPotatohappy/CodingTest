N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

cnt = 0
for i in range(N-M+1):
    tmp = A[i:i+M]
    tmp.sort()
    b_sort = sorted(B)
    tmp2 = 0
    for j in range(M):
        if tmp[j] == b_sort[j]:
            tmp2+=1
    if tmp2 == M:
        cnt+=1
    
print(cnt)
            