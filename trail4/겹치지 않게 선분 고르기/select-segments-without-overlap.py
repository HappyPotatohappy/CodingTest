n = int(input())
l = []

for _ in range(n):
    a, b = map(int, input().split())
    l.append([a,b])


def check(l1,l2):
    if l1[1] < l2[0] or l1[0] > l2[1]:
        return 1
    else:
        return 0

def check_tlt(l1,st):
    for i in st:
        if not check(l1,i):
            return 0
    return 1
st = []
mx = 0
def bt(bef_idx):
    global mx 

    mx = max(mx,len(st))

    for i in range(bef_idx,n):
        if check_tlt(l[i],st):
            st.append(l[i])
            bt(i+1)
            st.pop()
    return

bt(0)
print(mx)