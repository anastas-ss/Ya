#C - Телефонные номера
def sravni(tp_base, tp_new):
    for i in range(1, len(tp_new)):
        if tp_base[i] != tp_new[i]:
            return "NO"
    return "YES"

def clean(mystr):
    str_clean = ""
    for i in mystr:
        if i >= '0' and i <= '9':
            str_clean += i
    if len(str_clean) < 11:
        if str_clean[0] == '7' or str_clean[0] == '8':
            str_clean = str_clean[0] + '495' + str_clean[1:]
        else:
            str_clean = '7' + '495' + str_clean
    return str_clean

tp_new = clean(input())
tp1, tp2, tp3 = clean(input()), clean(input()), clean(input())

print(sravni(tp1, tp_new))
print(sravni(tp2, tp_new))
print(sravni(tp3, tp_new))