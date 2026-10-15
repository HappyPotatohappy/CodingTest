arr = list(map(int, input().split()))

arr.sort()

a = arr[0]
sum_abc = arr[6]
sum_bc = sum_abc - a
sum_ac = arr[4]
c = sum_ac - a
b = sum_bc - c

print(a,b,c)