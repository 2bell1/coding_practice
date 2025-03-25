def solution(land):
    row_size = len(land)
    col_size = len(land[0])
    
    # DP 배열을 사용하여 점수 계산
    for row in range(1, row_size):
        for col in range(col_size):
            # 각 칸에서 이전 행의 같은 열을 제외한 값 중에서 최댓값을 더함
            land[row][col] += max(land[row-1][(col+1)%4], land[row-1][(col+2)%4], land[row-1][(col+3)%4])
    
    # 마지막 행에서 가장 큰 값을 반환
    return max(land[row_size-1])

