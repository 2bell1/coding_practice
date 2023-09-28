R = input()
num = 0
i = 0
while i < len(R):
    if i < len(R):
        d = R[i]
        s = len(R)
        if i+1<len(R):
           if i+2<len(R):
             if (R[i+2]=="=") and (R[i+1] == "z")and (R[i] == "d"):
              i+=3
              num+=1
              continue
           
           if (R[i+1] == "=") or (R[i+1] == "-"):
              i += 2
              num+=1
           elif (R[i+1]=="j") and ((R[i] == "l") or (R[i] == "n")):
              i += 2
              num+=1
           else:
           
              i += 1
              num += 1
        else:
           
            i += 1
            num += 1 
       
print(num)