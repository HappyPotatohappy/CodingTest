import sys
input = sys.stdin.readline

n = int(input())
c = []
s = []
a_sc = 0
b_sc = 0
bef_cham = -1 #0: A, 1: B, 2:AB
cnt = 0
ctos = {"A" : 0, "B":1}
for _ in range(n):
    ci, si = input().split()
    si = int(si)
    ci = ctos[ci]
    if ci == 0:
        a_sc += si
    else:
        b_sc += si
    if a_sc==0 and b_sc==0 and bef_cham == -1:
        continue 
    if a_sc == b_sc and bef_cham != 2:
        bef_cham = 2
        cnt+=1
    elif a_sc > b_sc and bef_cham != 0:
        bef_cham = 0
        cnt+=1
    elif b_sc > a_sc and bef_cham != 1:
        bef_cham = 1
        cnt+=1

print(cnt)

