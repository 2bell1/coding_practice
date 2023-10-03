import sys

if __name__ == '__main__':

  num, des = map(int,input().split())
  arr = list(map(int, sys.stdin.readline().split())) 
  arr.sort()
  
  print(arr[des-1])