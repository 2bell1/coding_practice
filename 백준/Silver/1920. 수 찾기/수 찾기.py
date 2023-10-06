import sys

N=int(input())
N_arr = set(map(int, input().split()))
M=int(input())
numbers = input().split()
for number in numbers:
    i = int(number) 
    if i in N_arr:
        print(1)
    else:
        print(0)