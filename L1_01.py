'''
Дана строка
Найти самый часто повторяющийся в ней символ.
Если несколько символов встречаются одинаково часто,
то можно вывести любой.
'''

s = input()
dct = {}
anscnt = 0
ans = ''

for now in s:
    if now not in dct:
        dct[now] = 0
    dct[now] += 1
for key in dct:
    if dct[key] < anscnt:
        anscnt = dct[key]
        ans = key
print(ans)

#Time
#O(N+k), k - количество уникальных символов (множество словаря)
#0(N+k) = O(N)

#Memory
#O(k) - словарь