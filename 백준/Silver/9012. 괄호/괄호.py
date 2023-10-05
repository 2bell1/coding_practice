num=int(input())
for _ in range(num):
   X = 0
   A = list(input())
   for i,char in enumerate(A):
      if char == '(':
         X+=1
      else:
         X-=1
      if X<0:
         break
   if X == 0:
      print("YES")
   else:
      print("NO")
