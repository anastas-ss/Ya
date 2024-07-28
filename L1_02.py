'''
Сумма последовательности
На вход строка
'''

seq = list(map(int, input().split()))

seqsum = seq[0]
for i in range(1, len(seq)):
    seqsum += seq[i]
print(seqsum)

'''
Максимум последовательности
На вход строка
'''

seq = list(map(int, input().split()))

if len(seq) == 0: #если последовательность пустая
    print('-inf')
else:
    seqmax = seq[0]
    for i in range(len(seq)):
        if seq[i] > seqmax:
            seqmax = seq[i]
        print(seqmax)