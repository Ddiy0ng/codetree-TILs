i = input()
arr = i.split()
a, b, c = arr[0], arr[1], arr[2]
sum = int(a) + int(b) + int(c)
avg = sum // len(arr)
print(sum)
print(avg)
print(sum-avg)