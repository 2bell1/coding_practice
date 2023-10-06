import sys

num,target = map(int,input().split())
value =[]
ans=0
for _ in range(num):
  value.append(int(input()))
for i in range(num,0,-1):
   if (value[i-1]<=target):
      many=target//value[i-1]
      ans+=many
      target-=(value[i-1]*many)
print(ans)