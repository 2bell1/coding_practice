def solution(want, number, discount):
    answer = 0  # 상품이 원하는 대로 구입된 횟수를 저장할 변수
    N = len(discount)  # 할인 기간의 길이 (일수)
    disc_i = 0  # 할인 기간의 시작 인덱스
    
    while disc_i + 10 <= N:  # 할인 기간이 10일 이상인 경우에만 반복
        avail_disc = discount[disc_i:disc_i+10]  # 현재 10일 동안의 할인 목록
        
        # 각 제품과 그 제품이 필요한 수량을 비교
        if all(num == avail_disc.count(product) for product, num in zip(want, number)):
            answer += 1  # 원하는 수량이 충족되면 카운트

        disc_i += 1  # 다음 할인 기간을 확인하기 위해 인덱스를 증가시킴

    return answer  # 원하는 조건을 만족하는 기간의 수를 반환
