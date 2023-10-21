def solution(n):
    answer = []
    
    def hanoi(src, tgt, inter, n):
        if n == 1:
            answer.append([src, tgt])
        else:
            # 시작, 타겟, 중간 재귀함에 따라 계속 바뀜유의
            hanoi(src,inter,tgt,n-1) 
            hanoi(src,tgt,inter,1)  
            hanoi(inter,tgt,src,n-1) 
            
    hanoi(1,3,2,n)
    
    return answer
