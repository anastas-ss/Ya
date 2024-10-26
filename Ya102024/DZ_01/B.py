A = eval(input())
B = eval(input())
C = eval(input())
D = eval(input())
if A <= B and C <= D:
    print(A + 1, C + 1)
elif A >= B and C >= D:
    print(B + 1, D + 1)
elif A >= B and C <= D:
    if A + C <= B + D:
        print(A + 1, C + 1)
    else:
        print(B + 1, D + 1)
elif A <= B and C >= D:
    if A + C <= B + D:
        print(A + 1, C + 1)
    else:
        print(B + 1, D + 1)
