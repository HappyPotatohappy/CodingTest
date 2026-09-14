# 3중 for문 될듯
n = int(input())
arr = [int(input()) for _ in range(n)]

def nte(num):
    num_lst = list(map(int,list(str(num))))
    num_lst.reverse()
    return num_lst

def check(num1,num2,num3):
    num1lst = nte(num1)
    num2lst = nte(num2)
    num3lst = nte(num3)
    l1 = len(num1lst)
    l2 = len(num2lst)
    l3 = len(num3lst)
    mx = max(l1,l2,l3)
    n1 = [0]*mx
    n2 = [0]*mx
    n3 = [0]*mx
    for i in range(l1):
        n1[i] = num1lst[i]
    for i in range(l2):
        n2[i] = num2lst[i]
    for i in range(l3):
        n3[i] = num3lst[i]        
    for i,j,k in zip(n1,n2,n3):
        if i+j+k >= 10:
            return 0
    return 1
ans = -1
for i in range(n):
    for j in range(n):
        if i == j:
            continue
        for k in range(n):
            if j == k or k ==i :
                continue
            if check(arr[i],arr[j],arr[k]):
                ans = max(ans,arr[i]+arr[j]+arr[k])
print(ans)

