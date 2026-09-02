arr = list(map(int, input().split()))

arr.sort()
a = arr[0]
bppc = arr[-1] - a
c = bppc - arr[1]
b = arr[-2] - c

print(a,b,c)

