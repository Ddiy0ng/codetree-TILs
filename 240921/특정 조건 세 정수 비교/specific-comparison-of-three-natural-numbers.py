a = input()
arr = a.split()
n1 = arr[0]
n2 = arr[1]
n3 = arr[2]

if n1 <= n2 and n1 <= n3:
    a1 = 1
else:
    a1 = 0
if n1 == n2 and n2 == n3:
    a2 = 1
else:
    a2 = 0
print(a1, a2)