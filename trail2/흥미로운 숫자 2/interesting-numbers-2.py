X, Y = map(int, input().split())

## 처음에 나오는 수를 bef에 저장하고 한번 변화 할 때는 그대로 유지. 
## 한번 더 변할 때 여전히 bef와 같은지 확인
## 기본 컨셉은 변화하는 횟수를 카운트 하자

def check(num):
    cnt = 0
    numlst = list(map(int,str(num)))
    tmp = set(numlst)
    if len(tmp) != 2:
        return 0
    
    n = len(numlst)
    cklst = [0]*10
    tmp2 = []
    for i in numlst:
        cklst[i] +=1
    
    for j in range(10):
        if cklst[j] == 0:
            continue
        if cklst[j] != 0:
            tmp2.append(cklst[j])
    tmp2.sort()
    if tmp2[0] == 1 and tmp2[1] == n-1:
        return 1
    return 0

ans = 0
for i in range(X,Y+1):
    ans += check(i)
print(ans)