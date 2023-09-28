R = int(input())
S = []
E =[]
ANS = 0
isexist = False
for i in range(R):
    S.append(input())

for i in S:
    isexist = False
    E.clear()
    E.extend(list(i))
    exist = list()
    for char in E:
        
        if (char in exist) and (char != prev):
            isexist=True
            break
        else:
         exist.append(char)
         prev = char
    if isexist == False:
       ANS += 1
        
print(ANS)