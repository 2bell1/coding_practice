import sys

size = int(sys.stdin.readline())

arr=list()
for i in range(size):
  arr.append(int(sys.stdin.readline()))

arr.sort()
for i in range(size):
  
 print(arr[i])
