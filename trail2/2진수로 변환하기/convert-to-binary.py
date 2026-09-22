n = int(input())
ans = []
while 1:
    if n<2:
        ans.append(n)
        break
    
    ans.append(n%2)
    n = n//2
an = reversed(ans)
for i in an:
    print(i,end="")