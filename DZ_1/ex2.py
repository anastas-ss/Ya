a, b, c = int(input()), int(input()), int(input())

if a + b <= c:
    print("NO")
elif b + c <= a:
    print("NO")
elif a + c <= b:
    print("NO")
else:
    print("YES")