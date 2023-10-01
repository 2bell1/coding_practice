def solution(A,B):
    answer = 0
    A.sort(key=int); B.sort(key=int, reverse=True)
    for i in range(len(A)):
        answer += A[i]*B[i]
    return answer