mA, eA = map(int, input().split())
mB, eB = map(int, input().split())
if mA > mB:
    print('A')
elif mA == mB:
    if eA > eB:
        print('A')
    else:
        print('B')
else:
    print('B')