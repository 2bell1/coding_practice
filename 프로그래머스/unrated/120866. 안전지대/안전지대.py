def solution(board):
    answer = 0
    x = [-1, -1, -1, 0, 0, 1, 1, 1]
    y = [-1, 0, 1, -1, 1, -1, 0, 1]
    N = len(board)
    boom = []
    
    for i, c in enumerate(board):
        for i_, item in enumerate(board[i]):
            if item == 1:
                boom.append((i,i_))
    
    for i, (a,b) in enumerate(boom):
        for i_ in range(8):
            nx = a + x[i_]
            ny = b + y[i_]
            if 0<= nx < N and 0<= ny <N:
                board[nx][ny] = 1
                
    for i, c in enumerate(board):
        for i_, item in enumerate(board[i]): 
            if item == 0:
                answer += 1
                
    return answer