import sys
n=int(input())
x,y = [],[]

for _ in range(n):
    x_value, y_value = map(int, sys.stdin.readline().split())
    x.append(x_value)
    y.append(y_value)

x, y = zip(*sorted(zip(x, y), key=lambda a: (a[0], a[1])))
for a,b in zip(x,y):
    sys.stdout.write(f"{a} {b}\n")