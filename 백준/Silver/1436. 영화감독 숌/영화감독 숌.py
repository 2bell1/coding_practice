num = int(input())
Name = 666
i = 0
while i<num:
    check =0
    for x in range(len(str(Name))):
        if str(Name)[x] =="6":
           check +=1
        else:
            check =0
        
        if check == 3:
             break
    if check == 3:
       i+=1
       Name += 1
    else:
        Name+=1
        continue

print(Name-1)
