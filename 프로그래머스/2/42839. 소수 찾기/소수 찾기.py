import itertools

# ✅ 에라토스테네스의 체: 1~9999999까지 소수 판별
def sieve(limit):
    is_prime = [False, False] + [True] * (limit - 1) # 0 과 1은 소수가 아니므로 미리 설정 후 2부터 전부 True로 초기화하고 True일 시 소수로 판정
    for num in range(2, int(limit ** 0.5) + 1):
        if is_prime[num]:
            for multiple in range(num * num, limit + 1, num):
                is_prime[multiple] = False
    return is_prime

# ✅ 조합을 만들면서 소수 판별 (백트래킹)
def solution(numbers):
    max_num = 10**len(numbers)  # 최대 가능한 숫자 크기 (9999999)
    prime_table = sieve(max_num)  # 미리 소수 판별

    unique_numbers = set()
    
    # 모든 조합 만들기
    for length in range(1, len(numbers) + 1):
        for perm in itertools.permutations(numbers, length):
            num = int("".join(perm))
            unique_numbers.add(num)
    
    # 소수 개수 세기
    return sum(1 for num in unique_numbers if prime_table[num])
