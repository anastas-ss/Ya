#D - уравнение с корнем
#ax + b = c^2
#ax = c^2 - b
#x = (c^2 - b)/a
#ax + b > 0, c >= 0

a, b, c = int(input()), int(input()), int(input())

if c < 0:
    print("NO SOLUTION")
elif a == 0:
    if b == c**2:
        print("MANY SOLUTIONS")
    else:
        print("NO SOLUTION")
elif (c**2 - b)/a == (c**2 - b)//a:
    print((c**2 - b)//a)
else:
    print("NO SOLUTION")