s, p = map(int, input().split())
x = (s-int((s**2-4*p)**0.5))//2
y = (s+int((s**2-4*p)**0.5))//2
print(x, y)