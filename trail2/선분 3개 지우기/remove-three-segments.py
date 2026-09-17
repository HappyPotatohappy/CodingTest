n = int(input())
l = []
r = []
for _ in range(n):
    left, right = map(int, input().split())
    l.append(left)
    r.append(right)

##제거 할 것을 삼중 반복문 돌아도 될듯
def check(l1,l2):
    a1, b1 = l1[0], l1[1]
    a2, b2 = l2[0], l2[1]

    if a1 <= a2 <= b1 or a1 <= b2 <= b1 or a2 <= a1 <= b2 or a2 <= b1 <=b2:
        return 0
    return 1 

cnt = 0
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            is_inter = 1
            tmpl = l[:]
            tmpr = r[:]
            tmpl[i],tmpl[j],tmpl[k] = -1, -1, -1
            for s in range(n):
                if tmpl[s]==-1:
                    continue
                for o in range(s+1,n):
                    if tmpl[o]==-1:
                        continue
                    if check([tmpl[s],tmpr[s]],[tmpl[o],tmpr[o]]) == 0:
                        is_inter = 0
                        break
            if is_inter == 1:
                cnt+=1
print(cnt)