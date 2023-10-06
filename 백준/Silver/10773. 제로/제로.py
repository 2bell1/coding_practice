import sys

K=int(input())

arr=[]
sum=0
for i in range(K):
    num=int(input())
    if(num==0):
        arr.pop()
    else:
        arr.append(num)
for i,c in enumerate(arr):
    sum+=c
print(sum)