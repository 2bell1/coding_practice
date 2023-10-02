if __name__ == '__main__':
   num = int(input())
   sum=0
   who=0  #홀수 상근, 짝수 창영
   while sum < num:
      if((num-sum)%3==1):
         sum+=3
         who+=1
      else:
         sum+=1
         who+=1
   if (who%2==0):
      print("CY")
   else:
      print("SK")
      