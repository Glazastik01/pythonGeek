n = int(input('Введите количество кустов: '))
list = [int(x) for x in input( '-> ' ).split()]
n = len(list)
list = list + list[:2]
max = 0
for i in range(n):
    max = max(max, list[i] + list[i+1] + list[i+2])
print(max)