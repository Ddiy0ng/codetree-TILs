a, b = map(int, input().split())

if a < b:
    r1 = 1
else:
    r1 = 0
if a == b:
    r2 = 1
else:
    r2 = 0
print(r1, r2)