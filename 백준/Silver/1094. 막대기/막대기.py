import sys
sum=0
num = int(sys.stdin.readline())
short=64
i=0
while 1:
    if(short == num):
        i=1
        break
    if ((short/2)+sum) < num:
        short/=2
        sum += short
        i+=1
    elif ((short/2)+sum) == num:
        i+=1
        break
    else:
        short/=2
print(i)