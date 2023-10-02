if __name__ == '__main__':
   num = input()
   zeros,one=0,0
   flag=""
   for i in range(0,len(num)):
      if num[i] == '0':
         if flag == "zeros":
            continue
         zeros+=1
         flag="zeros"
      else:
         if flag == "one":
          continue
         one+=1
         flag="one"
   if(zeros<one):
      print(zeros)
   else:
      print(one)