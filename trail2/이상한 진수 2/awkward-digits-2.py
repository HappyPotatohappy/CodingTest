a = input()

def btot(bi):
    ans = 0
    n = len(bi)
    for i in range(n):
        ans += int(bi[i])*2**(n-i-1)
    return ans

n = len(a)
mx = 0
#aslt = list(map(int,list(a)))
for i in range(1,n):
    aslt = list(map(int,list(a)))
    if aslt[i]==0:
        aslt[i]=1
    else:
        aslt[i] = 0   
    mx = max(btot(aslt),mx)    

print(mx)