h, w = map(int, input().split()) #키, 몸무게
b = (10000*w)/(h**2)

if(b >= 25):
    print(f"{int(b)}\nObesity")