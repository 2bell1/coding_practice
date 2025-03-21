from itertools import product

def solution(word):
    answer = 0
    words = ['A', 'E', 'I', 'O', 'U']
    
    dic =[]
    for i in range(1,6):
        for combination in product(words,repeat=i):
            dic.append(''.join(combination))
    dic.sort()
    
    return dic.index(word)+1