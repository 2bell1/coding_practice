import sys

S, E, M = map(int, sys.stdin.readline().split())
a,b,c=0,0,0
year = 0
while 1:
    if(a==S) and (b==E) and(c==M):
        break
    a+=1;b+=1;c+=1
    if a==16:
        a = 1
    if b==29:
        b=1
    if c== 20:
        c=1
    year+=1
print(year)
    