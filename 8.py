n = int(input("Введите длинну шокаладки: "))
m = int(input("Введите шириину шокаладки: "))
k = int(input("Введите кол-во долек, которые хотите отломить: "))

if k < n * m and ((k % n == 0) or (k % m == 0)):
    print('да')
else:
    print('нет')