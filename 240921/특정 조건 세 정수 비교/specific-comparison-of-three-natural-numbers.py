a = input()
arr = a.split()
n1 = int(arr[0])
n2 = int(arr[1])
n3 = int(arr[2])

if n1 <= n2 and n1 <= n3:
    a1 = 1
else:
    a1 = 0
if n1 == n2 and n2 == n3:
    a2 = 1
else:
    a2 = 0
print(a1, a2)