X, Y = map(int, input().split())

def if_p(num1):
    num1 = list(map(int,str(num1)))
    num2 = num1[:]
    num2 = reversed(num2)

    for i,j in zip(num1,num2):
        if i != j:
            return 0
    return 1
cnt = 0
for i in range(X,Y+1):
    cnt+=if_p(i)
print(cnt)