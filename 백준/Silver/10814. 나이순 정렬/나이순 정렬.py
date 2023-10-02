import sys
num=int(input())
x,y = [],[]
for _ in range(num):
    x_value, y_value = map(str, sys.stdin.readline().split())
    x.append(int(x_value))
    y.append(y_value)
x, y = zip(*sorted(zip(x, y), key=lambda a: a[0]))
for a,b in zip(x,y):
    sys.stdout.write(f"{a} {b}\n")
    
