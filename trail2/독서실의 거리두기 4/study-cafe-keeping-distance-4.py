n = int(input())
seat = input()

seat = list(map(int,seat))
# 4중 for 문도 괜찮다
mx = 0
for i in range(n):
    if seat[i] == 1:
        continue
    for j in range(n):
        #위 두개는 어디에 넣을지를 결정하는 반복문
        if i == j:
            continue
        if seat[j] == 1:
            continue
        mn = 100
        seat[i], seat[j] = 1, 1
        for k in range(n):
            for l in range(k+1,n):
                if seat[k] == 1 and seat[l]==1:
                    ln = l - k
                    mn = min(mn,ln)
        seat[i], seat[j] = 0, 0
        mx = max(mn,mx)
print(mx)