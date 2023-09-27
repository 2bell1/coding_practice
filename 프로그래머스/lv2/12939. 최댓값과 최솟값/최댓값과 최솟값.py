def solution(s):
    if not s:
        return ""

    # 문자열을 공백을 기준으로 분리
    parts = s.split()
    
    # 분리된 부분 문자열 중에서 최소와 최대 값을 찾음
    n = min(parts, key=int)
    x = max(parts, key=int)
    
    answer = n + " " + x
    return answer
