import sys

A = int(sys.stdin.readline())
isseq = False
ans = 99
diff = 0
if A < 100:
    print(A)
else:
    for i in range(100,A+1):
        for a in range(len(str(i))-1):
             isseq=True
             pre = i
             i //= 10
             before_diff = diff
             diff = (pre%10)-(i%10)
             if before_diff != diff and a != 0:
                 isseq=False
                 break
        if isseq == True:
             ans+=1
    print(ans)
             