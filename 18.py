a = sorted(list(map(int, input().split())))
b = int(input())

res = []

for num, i in enumerate(a):
    if i >= b:
        if b - a[num - 1] > a[num] - b:
            res.append(a[num])
        else:
            res.append(a[num - 1])
            
if res:
    print(res[0])
else:
    print(max(a))