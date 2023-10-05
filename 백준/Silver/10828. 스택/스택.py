import sys
if __name__ == '__main__':
  num=int(sys.stdin.readline())

  st=[]
  for _ in range(num):
      method=sys.stdin.readline().split()

      if "push" == method[0]:
          st.append(method[1])
      elif method[0] == "pop":
          try:
            print(st.pop())
            
          except IndexError:
            print(-1)
      elif method[0] == "size":
          print(len(st))
      elif method[0] == "empty":
           if len(st) == 0:
               print(1)
           else:
               print(0)
      elif method[0] == "top":
          try:
              print(st[len(st)-1])
          except IndexError:
              print(-1)
