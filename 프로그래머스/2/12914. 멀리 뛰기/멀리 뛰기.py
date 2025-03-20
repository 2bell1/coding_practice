def solution(n):
    MOD = 1234567  # 나눠야 할 수
    
    # dp 배열 초기화
    dp = [0] * (n + 1)
    dp[0] = 1  # 0칸에 도달하는 방법은 1가지 (아무것도 안 뛰는 경우)
    
    for i in range(1, n + 1):
        # 1칸을 뛰는 경우
        dp[i] += dp[i - 1]
        # 2칸을 뛰는 경우
        if i >= 2:
            dp[i] += dp[i - 2]
        
        # 나머지 1234567로 나누기
        dp[i] %= MOD
    
    return dp[n]
