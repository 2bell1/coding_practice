def solution(n):
    answer = []
    
    def hanoi(src, tgt, inter, n):
        if n == 1:
            answer.append([src, tgt])
        else:
            hanoi(src,inter,tgt,n-1) #젤 위에까지 들어가서 중간으로 이동
            hanoi(src,tgt,inter,1)  #이동시키고 그 다음 위에꺼 3번로
            hanoi(inter,tgt,src,n-1) #이동시킨후 2번쨰꺼 3번쨰로
            
    hanoi(1,3,2,n)
    
    return answer