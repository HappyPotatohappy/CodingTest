a = input().strip()

num = list(map(int,list(a)))

n = len(num)
s = sum(num)
if s!=n:
    for i in range(n):
        if num[i] == 0:
            num[i]=1
            break
else:
    num[-1] = 0
ans = 0
for i in range(n):
    ans += 2**(n-i-1)*num[i]

print(ans)