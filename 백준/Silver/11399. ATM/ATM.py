import sys

num = int(input())
arr=list(map(int,sys.stdin.readline().split()))

arr.sort()
wait=[]
sum=0
a=0
for i,char in enumerate(arr):
    a+=int(char)
    wait.append(a)
for i,time in enumerate(wait):
    sum += time
print(sum)