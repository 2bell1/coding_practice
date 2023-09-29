import sys

fraction_location = 0 #분수의 열 위치
target_location =1 #목표수 위치
i =1
num_location=int(sys.stdin.readline().rstrip())

while 1:
  fraction_location +=1
  target_location += i
  if target_location > num_location:
    target_location -= i
    break
  i += 1
if (fraction_location % 2) ==0:
 numerator =1   #분자
 denominator =fraction_location  #분모
else:
  numerator =fraction_location   #분자
  denominator =1  #분모
for i in range(target_location, num_location):
  if (fraction_location % 2) ==0:
   numerator+=1
   denominator -=1
  else:
    numerator-=1
    denominator +=1

sys.stdout.write(f"{numerator}/{denominator}")