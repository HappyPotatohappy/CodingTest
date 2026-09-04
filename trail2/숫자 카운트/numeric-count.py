n = int(input())
a, b, c = [], [], []
for _ in range(n):
    num, cnt1, cnt2 = map(int, input().split())
    a.append(num)
    b.append(cnt1)
    c.append(cnt2)

def comp(num1,num2):
    l1 = list(str(num1))
    l2 = list(str(num2))
    cnt1 = 0
    cnt2 = 0
    for i in range(3):
        if l1[i] == l2[i]:
            cnt1+=1
        elif l1[i] in l2:
            cnt2+=1
    return cnt1, cnt2

num = list(range(1,10))
cand =[]
tlt = 0
for i in range(1,10):
    for j in range(1,10):
        for k in range(1,10):
            if i==j or j==k or i==k:
                continue
            s = i*100+j*10+k
            tmp = 0
            for l in range(n):
                cnt1, cnt2 = comp(s,a[l])
                if cnt1 == b[l] and cnt2 == c[l]:
                    tmp += 1
            if tmp == n:
                tlt += 1
print(tlt)


