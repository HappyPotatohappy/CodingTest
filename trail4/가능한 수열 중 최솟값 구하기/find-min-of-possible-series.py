n = int(input())
arr = []
cand = []

def print_answer(num_list):
    for i in num_list:
        print(i,end="")
    print()

def bt(loc):
    if loc == n+1:
        print_answer(arr)
        return 1
    
    for i in [4,5,6]:
        arr.append(i)
        if check(arr) !=0 and bt(loc+1):
            return 1
        arr.pop()
    return 0

def check(num_list):
    for k in range(n):
        if num_list[-k:] == num_list[-2*k:-k]:
            return 0

bt(1)
