a = input()
b = input()
arr1 = a.split()
arr2 = b.split()
m1 = int(arr1[0])
m2 = arr1[1]
n1 = int(arr2[0])
n2 = arr2[1]

if (m1 >= 19 and m2 =='M') or (n1 >= 19 and n2 == 'M'):
    print(1) 
else:
    print(0)