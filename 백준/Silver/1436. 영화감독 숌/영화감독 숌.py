num = int(input())
Name = 666
i = 0
t = True
while i<num:
    if "666" in str(Name):
       t=True
    else:
        t=False
    if t==True:
       i+=1
       Name += 1
    else:
        Name+=1
        continue

print(Name-1)
