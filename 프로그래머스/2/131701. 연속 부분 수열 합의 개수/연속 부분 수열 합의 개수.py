def solution(elements):
    answer = 0

    # 원형 수열을 처리하기 위해 배열을 두 배로 확장
    elements_x2 = elements * 2

    # 누적합 배열(prefix_sum) 초기화
    prefix_sum = [0 for _ in range(len(elements_x2))]
    prefix_sum[0] = elements_x2[0]

    # 누적합 배열 생성
    for i in range(1, len(elements_x2)):
        prefix_sum[i] = prefix_sum[i-1] + elements_x2[i]  

    nums = set()  # 서로 다른 부분 수열의 합을 저장할 집합

    # 길이가 1부터 len(elements)까지의 부분 수열의 합 계산
    for length in range(1, len(elements)+1):
        for i in range(len(elements)):  # 시작 인덱스
            # 부분 수열의 합을 누적합 배열을 이용해 구함
            sum = prefix_sum[i+length] - prefix_sum[i]
            nums.add(sum)  # 중복 방지를 위해 set에 추가

    # 가능한 서로 다른 부분 수열의 합 개수 반환
    answer = len(nums)
    return answer
