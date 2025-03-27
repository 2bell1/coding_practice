def solution(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    
    MOD = 1000000007
    a, b = 1, 2  # f(1), f(2) 초기값 설정
    
    for _ in range(3, n + 1):  # f(3)부터 f(n)까지 계산
        a, b = b, (a + b) % MOD  # 피보나치 방식으로 최적화
    
    return b
