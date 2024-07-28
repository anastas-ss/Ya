#A - кондиционер
type_work = ["freeze", "heat", "auto", "fan"]
t_room, t_cond = map(int, input().split())
ttype = input()
if ttype == type_work[3]:
    print(t_room)
elif ttype == type_work[2]:
    print(t_cond)
elif ttype == type_work[1]:
    if t_room < t_cond:
        print(t_cond)
    else:
        print(t_room)
elif ttype == type_work[0]:
    if t_room > t_cond:
        print(t_cond)
    else:
        print(t_room)