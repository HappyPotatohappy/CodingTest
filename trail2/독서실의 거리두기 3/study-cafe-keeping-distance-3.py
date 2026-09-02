import sys
input = sys.stdin.readline
n = int(input())
seats = input().strip()
seats = list(map(int,seats))
seats.insert(0,0) #무조건 1 부터 n까지의 인덱스로 관리 해야 함!!!!!!!

def check_longest_idx(numList):
    bef = -1
    leng = 0
    for i in range(1,n+1):
        if numList[i] and bef == -1:
            bef = i
        elif numList[i] and leng < i - bef:
            leng = i - bef
            idx = (i+bef)//2
            bef = i
        elif numList[i] and leng >= i - bef:
            bef = i
        
    return idx

idx = check_longest_idx(seats)


cop = seats[:]
mix = sys.maxsize
cop[idx] = 1
bef = -1
for i in range(1,n+1):
    if cop[i] and bef == -1:
        bef = i
    elif cop[i]:
        mix = min(mix,i-bef)
        bef = i
        
sys.stdout.write(str(mix))
