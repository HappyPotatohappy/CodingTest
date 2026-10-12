n = int(input())
seats = list(map(int,input()))

def get_dist(st_idx,ed_idx):
    return abs(ed_idx - st_idx)

def check_long(seat):
    dist_cand = []
    for i in range(n):
        if seats[i] == 1:
            for j in range(i+1,n):
                if seats[j] == 1:
                    dist_cand.append([j - i,i,j])
                    break
    dist_cand.sort(key = lambda x: -x[0])
    return dist_cand

def insert_one_mid(st_idx,ed_idx,seats):
    mid = (st_idx + ed_idx)//2
    seats[mid] = 1
    return seats
tmp2 = check_long(seats)
st_idx, ed_idx = tmp2[0][1], tmp2[0][2]
seats = insert_one_mid(st_idx, ed_idx,seats)
tmp3 = check_long(seats)
print(tmp3[-1][0])