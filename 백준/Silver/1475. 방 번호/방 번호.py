import math
num=int(input())
ls=[0]*10
for _ in range(len(str(num))):
    i=num%10
    if(i == 6 or i==9):
        ls[9]+=1
    else:
        ls[i]+=1
    num = int(num/10)
ls[9] = math.ceil(ls[9]/2)
ans = max(ls)
print(int(ans))
