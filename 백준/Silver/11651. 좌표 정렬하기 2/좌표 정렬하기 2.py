import sys
num = int(input())
x,y=[],[]
for _ in range(num):
    x_value, y_value = map(int,sys.stdin.readline().split())
    x.append(x_value)
    y.append(y_value)
x, y = zip(*sorted(zip(x, y), key=lambda a: (a[1], a[0])))
for a,b in zip(x,y):
    print(f"{a} {b}")
